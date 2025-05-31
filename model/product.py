class Product:
    def __init__(
        self,
        prCode=None,
        prName=None,
        buyPrice=None,
        sellPrice=None,
        inventory=None,
        desc=None,
    ):
        super().__init__()
        if prCode is not None:
            self.productCode = prCode
        else:
            self.productCode = None
        self.productName = prName
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice
        self.inventory = inventory
        self.description = desc
