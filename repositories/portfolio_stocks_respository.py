from DTO.portfolio_stocks import PortfolioStock
from helpers.query_builder import QueryBuilder
from helpers.sql import create_fields_values_params

class PortfolioStockRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def create(self, data: PortfolioStock):
        fields, values, params = create_fields_values_params(data.__dict__)
        query = f"INSERT INTO portfolio_stocks({fields}) VALUES({values}) RETURNING *"
        cursor = self.connection.cursor()
        cursor.execute(query, params)

        return dict(cursor.fetchone())
    
    def find(self, data: PortfolioStock = dict()):
        builder = QueryBuilder()

        builder.add(data.portfolio_id, "portfolio_id = ?")

        cursor = self.connection.cursor()
        query = f"""
            SELECT *
            FROM portfolio_stocks
            INNER JOIN stock ON portfolio_stocks.stock_id = stock.id
            {builder.where}
            """
        cursor.execute(query, builder.params)

        return cursor.fetchall()