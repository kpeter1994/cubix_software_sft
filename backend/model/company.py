from peewee import Model, CharField
from db.db_config import db

class Company(Model):
    symbol = CharField(unique=True)
    name = CharField()

    class Meta:
        database = db  # Az adatbázis, amelyet használsz (ez a db_config-ban van)
        table_name = "companies"  # A tábla neve

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "name": self.name
        }
