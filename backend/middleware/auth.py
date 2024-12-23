from functools import wraps
from flask import request, jsonify
from controller.auth_controller import AuthController

auth_controller = AuthController()

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Authorization header lekérése
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Hiányzó vagy érvénytelen token"}), 401

        token = auth_header.split("Bearer ")[1]
        payload = auth_controller.verify_token(token)

        if "error" in payload:
            return jsonify(payload), 401

        # Tokenből származó információk átadása
        kwargs["user"] = payload
        return f(*args, **kwargs)
    return decorated_function
