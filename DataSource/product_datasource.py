import sqlite3
from Model.product import Product
from Helper.database import Database


class ProductDataSource:

    def __init__(self, database: Database):
        self.database = database

    def addNewProduct(self, product:Product):
        cursor = self.database.con.cursor()
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
        self.database.con.commit()

    def getAllProducts(self):
        self.database.con.row_factory = sqlite3.Row
        cursor = self.database.con.cursor()

        products = []
        for row in cursor.execute("SELECT * FROM Product"):
            product = Product(
                prCode=int(row["prCode"]),
                prName=row["prName"],
                buyPrice=row["buyPrice"],
                sellPrice=row["sellPrice"],
                inventory=row["inventory"],
                desc=row["desc"],
            )
            products.append(product)

        return products

    def updateProductById(self, product: Product):
        cursor = self.database.con.cursor()
        query = """
            UPDATE Product
            SET prName = ?, buyPrice = ?, sellPrice = ?, inventory = ?, desc = ?
            WHERE prCode = ?
        """
        values = (
            product.productName,
            product.buyPrice,
            product.sellPrice,
            product.inventory,
            product.description,
            product.productCode,
        )
        cursor.execute(query, values)
        self.database.con.commit()