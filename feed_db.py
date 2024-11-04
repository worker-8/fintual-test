import requests
from repositories import create_uow
from DTO.stock import Stock
from DTO.stock_record_price import StockRecordPrice
from DTO.portfolio import Portfolio
from DTO.portfolio_stocks import PortfolioStock

def create_data():
    with create_uow() as uow:
        print('create data')

        print('create portfolios')

        nw_portfolio1 = Portfolio()
        nw_portfolio1.portfolio_name = "test1"
        rs_test1 = uow.portfolio_repository.create(data=nw_portfolio1)
        p_test1 = Portfolio(rs_test1)
        print(p_test1.__dict__)
        nw_portfolio2 = Portfolio()
        nw_portfolio2.portfolio_name = "test2"
        rs_test2 = uow.portfolio_repository.create(data=nw_portfolio2)
        p_test2 = Portfolio(rs_test2)
        print(p_test2.__dict__)

        nw_stock = Stock()
        nw_stock.symbol = 'IBM'
        
        rs = uow.stock_repository.create(data=nw_stock)
        stock = Stock(rs)

        nw_join1 = PortfolioStock()
        nw_join1.portfolio_id = p_test1.id
        nw_join1.stock_id = stock.id
        nw_join1.date_join = "2022-05-11"

        nw_join2 = PortfolioStock()
        nw_join2.portfolio_id = p_test2.id
        nw_join2.stock_id = stock.id
        nw_join2.date_join = "2020-05-11"

        uow.portfolio_stock_repository.create(data=nw_join1)
        uow.portfolio_stock_repository.create(data=nw_join2)

        data = get_data(stock.symbol)

        for record in data:
            row = data.get(record)
            nw_srp = StockRecordPrice()
            nw_srp.stock_id = stock.id
            nw_srp.stock_price = float(row['4. close'])
            nw_srp.date_price = record
            uow.stock_record_price_repository.create(data=nw_srp)
            


def get_data(symbol):
    # move api key toml
    api_key = 'XHL8FNX9JW2BB3AQ'
    # api_key = 'demo'
    url = f'''https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={symbol}&apikey={api_key}'''
    print(url)
    r = requests.get(url)
    data = r.json()

    return data['Time Series (Daily)']

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


# print(get_data('IBM'))
create_data()