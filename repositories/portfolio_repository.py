from DTO.portfolio import Portfolio
from helpers.query_builder import QueryBuilder
from helpers.sql import create_fields_values_params

class PortfolioRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def create(self, data: Portfolio):
        fields, values, params = create_fields_values_params(data.__dict__)
        query = f"INSERT INTO portfolio({fields}) VALUES({values}) RETURNING *"
        cursor = self.connection.cursor()
        cursor.execute(query, params)

        return dict(cursor.fetchone())
    
    def find(self, data: Portfolio = dict()):
        builder = QueryBuilder()
        builder.add(data.portfolio_name, "portfolio_name = ?")
        cursor = self.connection.cursor()
        query = f"""
            SELECT *
            FROM portfolio
            {builder.where}
            """
        cursor.execute(query, builder.params)

        return cursor.fetchall()