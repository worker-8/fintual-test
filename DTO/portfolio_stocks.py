class PortfolioStock:
    def __init__(self, data = dict()):
        self.id = data.get("id")
        self.portfolio_id = data.get("portfolio_id")
        self.stock_id = data.get("stock_id")
        self.date_join = data.get("date_join")