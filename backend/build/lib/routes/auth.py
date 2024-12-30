from flask import Blueprint, request, jsonify
from controller.auth_controller import AuthController
from model.user import User
from middleware.auth import auth_required

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    name = data.get("name")

    if not username or not password:
        return jsonify({"error": "Hiányzó felhasználónév vagy jelszó"}), 400

    response = AuthController.register(username, password, name)

    # Ha a response már egy dict, azt `jsonify`-zzuk, ha Response objektum, közvetlenül adjuk vissza
    if isinstance(response, dict):
        return jsonify(response), 201
    return response


@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Hiányzó felhasználónév vagy jelszó"}), 400

    user = AuthController().login(username, password)
    return jsonify(user), 200

@auth.route("/verification", methods=["GET"])
@auth_required
def verification(user):
    user_data = User.get_by_id(user["user_id"])
    return jsonify({"message": "Hozzáférés engedélyezve", "user": user_data.to_dict()}), 200
