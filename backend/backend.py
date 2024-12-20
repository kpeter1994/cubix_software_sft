from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB kliens csatlakozás
client = MongoClient("mongodb://admin:admin@mongodb-container:27017/")
db = client["portfolio_db"]

@app.route("/")
def home():
    return jsonify({"message": "Portfolio Manager Backend is running!"})

if __name__ == "__main__":
    app.run(debug=True)