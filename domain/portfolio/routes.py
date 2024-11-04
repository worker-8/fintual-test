from flask import Blueprint
from . import controller

def add_routes(parent: Blueprint) -> None:
    router = Blueprint("Portfolio", __name__, "/portfolio")

    router.add_url_rule("/", view_func=controller.fetch_portfolio)

    parent.register_blueprint(router)
