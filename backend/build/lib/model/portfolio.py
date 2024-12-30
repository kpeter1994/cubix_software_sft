from peewee import Model, IntegerField, CharField, TextField, DateTimeField, DoesNotExist
from datetime import datetime
from db.db_config import db

class Portfolio(Model):
    user_id = IntegerField()  # A felhasználó ID-ja
    name = CharField()  # Portfólió neve
    description = TextField(null=True)  # Leírás (opcionális)
    created_at = DateTimeField(default=datetime.now)  # Létrehozás időpontja

    class Meta:
        database = db  # Az adatbázis
        table_name = "portfolio"  # A tábla neve

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def create_portfolio(cls, user_id, name, description=None):
        try:
            portfolio = cls.create(
                user_id=user_id,
                name=name,
                description=description
            )
            return portfolio
        except Exception as e:
            raise Exception(f"Portfólió létrehozása sikertelen: {str(e)}")

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.select().where(cls.user_id == user_id)

