class MenuItem:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    @property
    def getItem(self):
        return self.item
    @property
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

