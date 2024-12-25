from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback
import yfinance as yf
from database import get_db_connection
from datetime import datetime
from stock import get_stock_data

portfolio_bp = Blueprint('portfolio', __name__)

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None
        self.change = None
        self.volume = None

    def update_data(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="1d")
        if not data.empty:
            self.price = data['Close'][0]
            self.change = data['Close'][0] - data['Open'][0]
            self.volume = data['Volume'][0]

@portfolio_bp.route("/", methods=["GET"])
@jwt_required()
def get_portfolio():
    try:
        current_user = get_jwt_identity()

        with get_db_connection() as conn:
            user = conn.execute(
                "SELECT id FROM users WHERE username = ?",
                (current_user,)
            ).fetchone()

            if not user:
                return jsonify({"message": "User not found"}), 404

            user_id = user["id"]

            portfolio = conn.execute(
                "SELECT stock_ticker, close_price, open_price, high_price, low_price, volume, date_added FROM portfolio WHERE user_id = ?",
                (user_id,)
            ).fetchall()

        portfolio_data = []
        for row in portfolio:
            # Konvertáljuk a byte típusú adatokat stringé vagy integeré
            volume = row["volume"]
            if isinstance(volume, bytes):
                volume = int.from_bytes(volume, 'little')

            portfolio_data.append({
                "ticker": row["stock_ticker"],
                "price": row["close_price"],
                "open_price": row["open_price"],
                "high_price": row["high_price"],
                "low_price": row["low_price"],
                "volume": volume,
                "date_added": row["date_added"],
            })

        return jsonify({"portfolio": portfolio_data}), 200

    except Exception as e:
        print(f"Error fetching portfolio: {e}")
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500
@portfolio_bp.route("/add", methods=["POST"])
@jwt_required()
def add_to_portfolio():
    try:
        current_user = get_jwt_identity()
        data = request.get_json()
        stock_ticker = data.get("stock_ticker")

        if not stock_ticker:
            return jsonify({"message": "Stock ticker is required"}), 400

        with get_db_connection() as conn:
            user = conn.execute(
                "SELECT id FROM users WHERE username = ?",
                (current_user,)
            ).fetchone()

            if not user:
                return jsonify({"message": "User not found"}), 404

            user_id = user["id"]

            stock = yf.Ticker(stock_ticker)
            stock_data = stock.history(period="1d")

            if stock_data.empty:
                return jsonify({"message": "Stock data not found"}), 404

            close_price = stock_data['Close'][0]
            open_price = stock_data['Open'][0]
            high_price = stock_data['High'][0]
            low_price = stock_data['Low'][0]
            volume = stock_data['Volume'][0]
            date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            conn.execute(
                """
                INSERT INTO portfolio (user_id, stock_ticker, close_price, open_price, high_price, low_price, volume, date_added)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, stock_ticker, close_price, open_price, high_price, low_price, volume, date_added)
            )
            conn.commit()

        return jsonify({"message": "Stock added to portfolio"}), 200

    except Exception as e:
        print(f"Error adding stock to portfolio: {e}")
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500

@portfolio_bp.route("/stock/<ticker>", methods=["GET"])
def get_stock_info(ticker):
    stock_data = get_stock_data(ticker)
    return jsonify(stock_data), 200
