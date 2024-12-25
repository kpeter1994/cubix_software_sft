from database import get_db_connection


def recreate_table():
    try:
        with get_db_connection() as conn:
            # Töröljük a már meglévő táblát
            conn.execute("DROP TABLE IF EXISTS portfolio")

            # Új tábla létrehozása a szükséges oszlopokkal
            conn.execute("""
                CREATE TABLE portfolio (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    stock_ticker TEXT,
                    close_price REAL,
                    open_price REAL,
                    high_price REAL,
                    low_price REAL,
                    volume INTEGER,
                    date_added TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            conn.commit()
            print("Table recreated successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")


recreate_table()
