import sqlite3
import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS
import bcrypt
import os

app = Flask(__name__)
CORS(app)

# SQLite adatbázis elérési út a gyökérkönyvtár "data" mappájában
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # A script helye
DATA_DIR = os.path.join(BASE_DIR, "../data")  # Gyökér mappa "data" könyvtára
DATABASE_PATH = os.path.join(DATA_DIR, "portfolio.db")

# Ellenőrizzük, hogy létezik-e a mappa, ha nem, létrehozzuk
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row  # Eredmények dictionary-ként való eléréséhez
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error ({DATABASE_PATH}): {e}")
        raise

# Users tábla inicializálása
def initialize_database():
    try:
        with get_db_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    passwordHash TEXT NOT NULL
                );
            """)
            conn.commit()
            print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        traceback.print_exc()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        # Felhasználó keresése az SQLite-ban
        with get_db_connection() as conn:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            ).fetchone()

        if not user:
            return jsonify({"message": "Invalid username or password"}), 401

        stored_password_hash = user["passwordHash"]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            return jsonify({"message": "Login successful", "userId": user["id"]}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401

    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        # Jelszó titkosítása
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO users (username, passwordHash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()

        return jsonify({"message": "User added successfully"}), 201

    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500

if __name__ == "__main__":
    # Adatbázis inicializálása induláskor
    initialize_database()
    app.run(debug=True, host="0.0.0.0")
