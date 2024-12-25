from flask import Blueprint, jsonify, request
from database import get_db_connection
import bcrypt
import traceback
from token_manager import generate_token  # Importáljuk a token generálást
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
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
                (username, password_hash.decode('utf-8'))
            )
            conn.commit()

        # Token generálása a regisztráció után
        token_obj = generate_token({"username": username})
        return jsonify({"message": "User added successfully", "token": token_obj.token, "expiration": token_obj.expiration}), 201

    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists"}), 400

    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500

@auth_bp.route("/login", methods=["POST"])
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
            # Token generálása
            token_obj = generate_token({"username": username})
            return jsonify({"message": "Login successful", "token": token_obj.token, "expiration": token_obj.expiration}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401

    except Exception as e:
        print(f"Error during login: {e}")
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500
