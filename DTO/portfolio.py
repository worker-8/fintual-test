class Portfolio:
    def __init__(self, data = dict()):
        self.id = data.get('id')
        self.portfolio_name = data.get('portfolio_name')