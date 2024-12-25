from db.db_config import db
from peewee import Model, CharField
import bcrypt


class User(Model):

    username = CharField(unique=True)
    password = CharField()
    name = CharField(null=True)

    class Meta:
        database = db
        table_name = "users"


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name
        }

    def check_password(self, password: set) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    @classmethod
    def create_user(cls, username, password, name):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return cls.create(username=username, password=hashed_password, name=name)

    @classmethod
    def get_by_id(cls, user_id):
        try:
            return cls.get(cls.id == user_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_by_username(cls, username):
        try:
            return cls.get(cls.username == username)
        except cls.DoesNotExist:
            return None



