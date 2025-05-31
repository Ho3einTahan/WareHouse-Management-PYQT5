import sqlite3
from Model.product import Product

class Database():

    def __init__(self):
        self.con = sqlite3.connect("warehouse.db")
        self._create_tables()

    def _create_tables(self):
        cursor = self.con.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Product (
                prCode INTEGER PRIMARY KEY AUTOINCREMENT,
                prName TEXT NOT NULL,
                buyPrice REAL,
                sellPrice REAL,
                inventory INTEGER,
                desc TEXT
            )
        """
        )

        self.con.commit()

    def close(self):
        self.con.close()