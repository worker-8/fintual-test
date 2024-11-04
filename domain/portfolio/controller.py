from flask import request

def fetch_portfolio():
    # returns all portfolios
    return {"status": True, "test": "test"}

def fetch_profit(portfolio_name):
    # returns the profit of a portfolio over a period of time
    return {"status": True, "test": portfolio_name}

def fetch_annualized_return(portfolio_name):
    # returns the profit of an annualized portfolio
    return {"status": True, "test": portfolio_name}