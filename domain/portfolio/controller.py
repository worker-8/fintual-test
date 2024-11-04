from datetime import datetime, timedelta
from flask import request
from repositories import create_uow

from DTO.portfolio import Portfolio
from DTO.portfolio_stocks import PortfolioStock
from DTO.stock_record_price import StockRecordPrice

def fetch_portfolio():
    with create_uow() as uow:
        ouput = []
        portfolios = uow.portfolio_repository.find(data=Portfolio())
        list = [Portfolio(dict(p)) for p in portfolios]
        
        for e in list:
            PStock = PortfolioStock()
            PStock.portfolio_id = e.id

            stocks = uow.portfolio_stock_repository.find(data=PStock)

            data = {
                "id": e.id,
                "name": e.portfolio_name,
                "stocks": [dict(s) for s in stocks]
            }
            
            ouput.append(data)
        
        return {"status": True, "result": ouput}

def fetch_profit(portfolio_name):
    # returns the profit of a portfolio over a period of time
    initial = request.args.get('initial')
    end = request.args.get('end')
    with create_uow() as uow:
        # output stocks profit
        output = []

        data = Portfolio()
        data.portfolio_name=portfolio_name
        # get portfolio
        rsPortfolio = uow.portfolio_repository.find(data=data)
        
        
        if len(rsPortfolio) == 0:
            #early return if portfolio not exist
            return ({"status": False, "msg": "Portfolio Not Found"}, 404)
        
        portfolio = Portfolio(data=dict(rsPortfolio[0]))

        # find stocks
        PStocks = PortfolioStock()
        PStocks.portfolio_id = portfolio.id
        rsPortfolioStocks = uow.portfolio_stock_repository.find(data=PStocks)

        if len(rsPortfolioStocks) == 0:
            #early return if portfolio not has stocks
            return ({"status": False, "msg": "Portfolio Not Found stocks"}, 404)
        
        stocks = [dict(s) for s in rsPortfolioStocks]
        
        for stock in stocks:
            # may explode if dates are not found
            srp = StockRecordPrice()
            srp.stock_id = stock.get("stock_id")
            srp.date_price = initial
            init_data = find_data_stock(uow, srp)
            
            srp.date_price = end
            end_data = find_data_stock(uow, srp)

            if (init_data == False or end_data == False):
                output.append({"symbol": stock.get('symbol'), "msg": "Data Miss Match, check dates"})
                continue
            init_value =  init_data.get('stock_price')
            end_value = end_data.get('stock_price')
            
            output.append({
                "symbol": stock.get('symbol'),
                "init_data":init_data,
                "end_data":end_data,
                "delta": end_value - init_value,
                "delta%": ((end_value - init_value)/init_value) * 100
            })

        return {"status": True, "test": portfolio_name, "stocks": output}

def fetch_annualized_return(portfolio_name):
    # returns the profit of an annualized portfolio
    return {"status": True, "test": portfolio_name}

def find_data_stock(uow, srp:StockRecordPrice, attemp = 1):
    initial_price_rs = uow.stock_record_price_repository.find(data=srp)
    if attemp == 5:
        return False

    if len(initial_price_rs) == 0:
        srp.date_price = date_add_1(srp.date_price)
        return find_data_stock(uow, srp, attemp=attemp +1)
    
    return dict(initial_price_rs[0])

def date_add_1(date):
    splited = date.split('-')
    old_date = datetime(int(splited[0]),int(splited[1]),int(splited[2]))
    nw_date = old_date + timedelta(days = 1)
    # date.strftime('%Y-%m-%d')
    return nw_date.strftime('%Y-%m-%d')