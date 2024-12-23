from flask import Flask, request, jsonify
from controller.auth_controller import AuthController
from model.user import User
from middleware.auth import auth_required

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API!"}), 200

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Hiányzó felhasználónév vagy jelszó"}), 400

    if User.get_by_username(username):
        return jsonify({"error": "A felhasználónév már foglalt"}), 409

    user = AuthController().register(username, password)
    return user, 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Hiányzó felhasználónév vagy jelszó"}), 400

    user = AuthController().login(username, password)
    return user, 200

@app.route("/protected", methods=["GET"])
@auth_required
def protected_resource(user):
    return jsonify({"message": "Hozzáférés engedélyezve", "user_id": user["user_id"]}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")