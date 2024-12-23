import sqlite3
import os


class DB:
    _connection = None
    _db_name = os.path.join(os.path.dirname(__file__), "../db/portfolio.db")

    @staticmethod
    def _get_connection():
        if DB._connection is None:
            DB._connection = sqlite3.connect(DB._db_name)
            DB._connection.row_factory = sqlite3.Row
        return DB._connection

    @staticmethod
    def insert(table, data):
        connection = DB._get_connection()
        keys = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(table, record_id):
        connection = DB._get_connection()
        query = f"SELECT * FROM {table} WHERE id = ?"
        cursor = connection.cursor()
        cursor.execute(query, (record_id,))
        result = cursor.fetchone()
        return dict(result) if result else None

    @staticmethod
    def get_by_field(table, field, value):
        connection = DB._get_connection()
        query = f"SELECT * FROM {table} WHERE {field} = ?"
        cursor = connection.cursor()
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        return dict(result) if result else None
