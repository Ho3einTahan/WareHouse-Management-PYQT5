from DataSource.product_datasource import ProductDataSource
from Model.product import Product


class ProductRepository:

    def __init__(self, productDataSource: ProductDataSource):
        self.productDataSource = productDataSource

    def addNewProduct(self, product: Product):
        self.productDataSource.addNewProduct(product)

    def getAllProducts(self):
        return self.productDataSource.getAllProducts()

    def updateProduct(self, product: Product):
        self.productDataSource.updateProductById(product)
    
    def deleteProduct(self,prCode):
        self.productDataSource.deleteProductById(prCode)