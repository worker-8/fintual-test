from flask import request
from repositories import create_uow

from DTO.portfolio import Portfolio
from DTO.portfolio_stocks import PortfolioStock

def fetch_portfolio():
    with create_uow() as uow:
        ouput = []
        portfolios = uow.portfolio_repository.find()
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
    return {"status": True, "test": portfolio_name}

def fetch_annualized_return(portfolio_name):
    # returns the profit of an annualized portfolio
    return {"status": True, "test": portfolio_name}