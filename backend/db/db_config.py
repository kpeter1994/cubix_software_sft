import os
from peewee import SqliteDatabase

db_name = os.path.join(os.path.dirname(__file__), "../db/portfolio.db")
db = SqliteDatabase(db_name)