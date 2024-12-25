from flask_jwt_extended import create_access_token
from datetime import timedelta

class Token:
    def __init__(self, token, expiration):
        self.token = token
        self.expiration = expiration

def generate_token(identity):
    access_token = create_access_token(identity=identity["username"], expires_delta=timedelta(hours=1))
    expiration = (timedelta(hours=1).total_seconds() + 3600)
    return Token(access_token, expiration)
