from flask import Blueprint, request, jsonify
import yfinance as yf
import json
from middleware.auth import auth_required

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
