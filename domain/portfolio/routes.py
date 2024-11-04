from flask import Blueprint
from . import controller

def add_routes(parent: Blueprint) -> None:
    router = Blueprint("Portfolio", __name__, "/portfolio")

    router.add_url_rule("/portfolio", view_func=controller.fetch_portfolio)
    router.add_url_rule("/portfolio/<portfolio_name>/profit", view_func=controller.fetch_profit)
    router.add_url_rule("/portfolio/<portfolio_name>/annualized_return", view_func=controller.fetch_annualized_return)

    parent.register_blueprint(router)
