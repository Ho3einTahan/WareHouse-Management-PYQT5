import sqlite3
from model.product import Product


class Database:

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

    def addNewProduct(self, product):
        cursor = self.con.cursor()
        cursor.execute(
            "INSERT INTO Product (prName, buyPrice, sellPrice, inventory, desc) VALUES (?, ?, ?, ?, ?)",
            (
                product.productName,
                product.buyPrice,
                product.sellPrice,
                product.inventory,
                product.description,
            ),
        )
        self.con.commit()

    def getAllProduct(self):
        cursor = self.con.cursor()
        cursor.execute(
            """
                SELECT * FROM Product
            """
        )
        rows = cursor.fetchall()
        products = []

        for row in rows:
            product = Product(
                prCode=row["prCode"],
                prName=row["prName"],
                buyPrice=row["buyPrice"],
                sellPrice=row["sellPrice"],
                inventory=row["inventory"],
                desc=row["desc"],
            )
            
            products.append(product)

        print(products)

    def updateProductById(self, product):
        cursor = self.con.cursor()
        query = """
    UPDATE Product
        SET prName = ?, buyPrice = ?, sellPrice = ?, inventory = ?, description = ?
    WHERE prId = ?
        """
        values = (
            product["prName"],
            product["buyPrice"],
            product["sellPrice"],
            product["inventory"],
            product["desc"],
            product["prCode"],
        )
        cursor.execute(query, values)
        self.con.commit()

    def close(self):
        self.con.close()
