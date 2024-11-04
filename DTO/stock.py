class Stock:
    def __init__(self, data = dict()):
        self.id = data.get("id")
        self.symbol = data.get("symbol")