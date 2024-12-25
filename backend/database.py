import os
import sqlite3
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
DATABASE_PATH = os.path.join(DATA_DIR, "portfolio.db")

# Ellenőrizzük, hogy létezik-e a data mappa, ha nem, létrehozzuk
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row  # Eredmények dictionary-ként való eléréséhez
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error ({DATABASE_PATH}): {e}")
        raise

def initialize_database():
    try:
        with get_db_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    passwordHash TEXT NOT NULL
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS portfolio (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    stock_ticker TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                );
            """)
            conn.commit()
            print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        traceback.print_exc()

