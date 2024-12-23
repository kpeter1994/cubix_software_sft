from db.db import DB
import bcrypt


class User:

    def __init__(self, user_id=None, username=None, password=None):
        self.id = user_id
        self.username = username
        self.password = password

    @classmethod
    def get_by_username(cls, username):
        user_data = DB.get_by_field("users", "username", username)
        if user_data:
            return cls(
                user_id=user_data["id"],
                username=user_data["username"],
                password=user_data["password"]
            )
        return None

    @classmethod
    def create(cls, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_id = DB.insert("users", {"username": username, "password": hashed_password})
        return cls.get_by_id(user_id)

    @classmethod
    def get_by_id(cls, user_id):
        user_data = DB.get_by_id("users", user_id)
        if user_data:
            return cls(
                user_id=user_data["id"],
                username=user_data["username"],
                password=user_data["password"]
            )
        return None

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

