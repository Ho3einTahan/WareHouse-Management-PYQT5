class Product:
    def __init__(self, prCode, prName, buyPrice, sellPrice, inventory, desc):
        self.productCode = prCode
        self.productName = prName
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice
        self.inventory = inventory
        self.description = desc