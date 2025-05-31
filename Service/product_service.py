from Model.product import Product
from Repository.product_repository import ProductRepository


class ProductService:

    def __init__(self, product_repository: ProductRepository):
        self.repo = product_repository

    def create_product(self, prName, buyPrice, sellPrice, inventory, desc):
        if buyPrice < 0 or sellPrice < 0 or inventory < 0:
            raise ValueError("قیمت و موجودی نمی‌تواند منفی باشد")

        product = Product(
            prName=prName,
            buyPrice=buyPrice,
            sellPrice=sellPrice,
            inventory=inventory,
            desc=desc,
        )

        self.repo.addNewProduct(product)

    def list_products(self):
        return self.repo.getAllProducts()

    def update_product(self, product):
        self.repo.updateProduct(product)