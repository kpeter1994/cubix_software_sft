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
    user_id = user["user_id"]
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
    user_id = user["user_id"]
    portfolios = PortfolioController.get_user_portfolios(user_id)

    # Ha nincs portfólió, térjen vissza üres tömbbel
    if not portfolios:
        return jsonify({"portfolios": []}), 200

    return jsonify({"portfolios": portfolios}), 200

@stock.route("/add-shares-to-portfolio", methods=["POST"])
@auth_required
def add_shares_to_portfolio(user):
    user_id = user["user_id"]
    request_data = request.get_json()

    portfolio_id = request_data.get("portfolio_id")
    share_data = request_data.get("share_data", [])

    if not portfolio_id or not share_data:
        return jsonify({"error": "Portfolio ID és share_data szükséges"}), 400

    result = PortfolioController.add_shares_to_portfolio(user_id, portfolio_id, share_data)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 201

@stock.route("/get-shares-for-portfolio", methods=["GET"])
@auth_required
def get_shares_for_portfolio(user):
    user_id = user["user_id"]
    portfolio_id = request.args.get("portfolio_id")

    if not portfolio_id:
        return jsonify({"error": "Portfolio ID szükséges"}), 400

    portfolio = PortfolioController.get_portfolio(portfolio_id)

    if "error" in portfolio:
        return jsonify(portfolio), 404

    if portfolio["user_id"] != user_id:
        return jsonify({"error": "Ez a portfólió nem a felhasználóhoz tartozik"}), 403

    shares = Share.get_by_portfolio_id(portfolio_id)

    return jsonify({"shares": [share.to_dict() for share in shares]}), 200

@stock.route("/delete-portfolio", methods=["DELETE"])
@auth_required
def delete_portfolio(user):
    user_id = user["user_id"]
    portfolio_id = request.args.get("portfolio_id")

    if not portfolio_id:
        return jsonify({"error": "Portfolio ID szükséges"}), 400

    try:
        portfolio_id = int(portfolio_id)
    except ValueError:
        return jsonify({"error": "Érvénytelen Portfolio ID"}), 400

    result = PortfolioController.delete_portfolio(user_id, portfolio_id)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 200


@stock.route("/delete-share-from-portfolio", methods=["DELETE"])
@auth_required
def delete_share_from_portfolio(user):
    user_id = user["user_id"]
    portfolio_id = request.args.get("portfolio_id")
    share_id = request.args.get("share_id")

    if not portfolio_id or not share_id:
        return jsonify({"error": "Portfolio ID és Share ID szükséges"}), 400

    result = PortfolioController.delete_share_from_portfolio(user_id, portfolio_id, share_id)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 200

@stock.route("/get-portfolio-details", methods=["GET"])
@auth_required
def get_portfolio_details(user):
    portfolio_id = request.args.get("portfolio_id")
    if not portfolio_id:
        return jsonify({"error": "Portfolio ID szükséges"}), 400

    portfolio_details = PortfolioController.get_portfolio_details(portfolio_id)

    return jsonify({"portfolio_details": portfolio_details}), 200

@stock.route("/current-price", methods=["GET"])
@auth_required
def get_current_price(user):
    stock_symbol = request.args.get("stock_symbol")
    if not stock_symbol:
        return jsonify({"error": "A részvény szimbólum megadása kötelező"}), 400

    result = PortfolioController.get_current_stock_price(stock_symbol)

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result), 200

@stock.route("/search", methods=["GET"])
@auth_required
def search_stock(user):
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Keresési kifejezés megadása kötelező"}), 400

    result = PortfolioController.search_stock(query)

    if "error" in result:
        return jsonify(result), 404

    return jsonify(result), 200
