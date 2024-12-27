from flask import Blueprint, request, jsonify
import yfinance as yf
import json
from middleware.auth import auth_required
from controller.portfolio_controller import PortfolioController
from model.share import Share

stock = Blueprint("stock", __name__)

@stock.route("/history-price", methods=["GET"])
@auth_required
def history_price(user):
    stock_symbol = request.args.get("stock_symbol")
    start = request.args.get("start")
    end = request.args.get("end")
    interval = "1d"

    def get_historical_prices_processed(symbol, start_date, end_date, interval="1d"):
        stock = yf.Ticker(symbol)
        data = stock.history(start=start_date, end=end_date, interval=interval)
        if not data.empty:
            processed_data = [
                {
                    "x": row["Date"].strftime("%Y-%m-%d"),  # Dátum stringként
                    "y": [row["Open"], row["High"], row["Low"], row["Close"]],  # Gyertyatartó értékek
                }
                for _, row in data.reset_index().iterrows()
            ]
            return {"symbol": symbol, "data": processed_data}
        else:
            return {"error": "Nem található adat a megadott időszakra."}

    historical_data = get_historical_prices_processed(stock_symbol, start, end, interval)

    return jsonify(historical_data), 200

@stock.route("/create-portfolio", methods=["POST"])
@auth_required
def create_portfolio(user):
    user_id = user["user_id"]  # A middleware biztosítja a hitelesített felhasználót
    request_data = request.get_json()

    name = request_data.get("name")
    description = request_data.get("description")

    if not name:
        return jsonify({"error": "A portfólió név megadása kötelező"}), 400

    result = PortfolioController.create_portfolio(user_id, name, description)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 201


@stock.route("/get-user-portfolios", methods=["GET"])
@auth_required
def get_user_portfolios(user):
    user_id = user["user_id"]  # A hitelesített felhasználó ID-ja

    # Lekérjük a felhasználó összes portfólióját
    portfolios = PortfolioController.get_user_portfolios(user_id)

    if not portfolios:
        return jsonify({"error": "Nincsenek portfóliók a felhasználóhoz"}), 404

    return jsonify({"portfolios": portfolios}), 200


@stock.route("/add-shares-to-portfolio", methods=["POST"])
@auth_required
def add_shares_to_portfolio(user):
    user_id = user["user_id"]  # A hitelesített felhasználó ID-ja
    request_data = request.get_json()

    portfolio_id = request_data.get("portfolio_id")
    share_data = request_data.get("share_data", [])

    # Ellenőrizzük, hogy a portfolio_id és a share_data meg vannak-e adva
    if not portfolio_id or not share_data:
        return jsonify({"error": "Portfolio ID és share_data szükséges"}), 400

    # Hívjuk meg a controller-t, hogy hozzáadja a részvényeket a portfólióhoz
    result = PortfolioController.add_shares_to_portfolio(user_id, portfolio_id, share_data)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 201

@stock.route("/get-shares-for-portfolio", methods=["GET"])
@auth_required
def get_shares_for_portfolio(user):
    user_id = user["user_id"]
    portfolio_id = request.args.get("portfolio_id")  # Az URL query paraméterekből

    # Ellenőrizzük, hogy a portfolio_id meg van-e adva
    if not portfolio_id:
        return jsonify({"error": "Portfolio ID szükséges"}), 400

    # Lekérjük a portfóliót és ellenőrizzük, hogy az aktuális felhasználóhoz tartozik-e
    portfolio = PortfolioController.get_portfolio(portfolio_id)

    if "error" in portfolio:
        return jsonify(portfolio), 404

    if portfolio["user_id"] != user_id:
        return jsonify({"error": "Ez a portfólió nem a felhasználóhoz tartozik"}), 403

    # Lekérjük a portfólióhoz tartozó részvényeket
    shares = Share.get_by_portfolio_id(portfolio_id)

    return jsonify({"shares": [share.to_dict() for share in shares]}), 200
