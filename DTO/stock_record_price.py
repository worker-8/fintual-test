class StockRecordPrice:
    def __init__(self, data = dict()):
        self.id = data.get("id")
        self.stock_id = data.get("stock_id")
        self.stock_price = data.get("stock_price")
        self.date_price = data.get("date_price")