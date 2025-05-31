from Helper.database import Database
from DataSource.product_datasource import ProductDataSource
from Repository.product_repository import ProductRepository
from Service.product_service import ProductService

# create instance
database = Database()
product_data_source = ProductDataSource(database)
product_repository = ProductRepository(product_data_source)
product_service = ProductService(product_repository)