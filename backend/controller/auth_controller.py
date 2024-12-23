from model.user import User
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "your_secret_key"

class AuthController:
    def register(self, username, password):
        if User.get_by_username(username):
            return {"error": "Ez a felhasználónév már foglalt"}
        user = User.create(username, password)
        return {"id": user.id, "username": user.username}

    def generate_token(self, user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def login(self, username, password):
        user = User.get_by_username(username)
        if user and user.check_password(password):
            token = self.generate_token(user.id)
            return {"token": token, "message": "Login successful"}
        return {"error": "Invalid username or password"}

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}

