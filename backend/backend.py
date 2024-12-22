from flask import Flask, jsonify, request
from pymongo import MongoClient
import bcrypt
import os
import traceback

app = Flask(__name__)

# MongoDB URI környezeti változóból
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/portfolio")
client = MongoClient(mongo_uri)
db = client.get_database()
users_collection = db["users"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

@app.route("/login", methods=["POST"])
def login():
    try:
        # Kérésből adatok beolvasása
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        # Felhasználó keresése
        user = users_collection.find_one({"username": username})
        if not user:
            return jsonify({"message": "Invalid username or password"}), 401

        # Jelszó hash ellenőrzése
        stored_password_hash = user["passwordHash"].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            return jsonify({"message": "Login successful", "userId": str(user["_id"])}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401

    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
