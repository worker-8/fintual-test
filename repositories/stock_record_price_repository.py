from DTO.stock_record_price import StockRecordPrice
from helpers.query_builder import QueryBuilder
from helpers.sql import create_fields_values_params

class StockRecordPriceRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def create(self, data: StockRecordPrice):
        fields, values, params = create_fields_values_params(data.__dict__)
        query = f"INSERT INTO stock_record_price({fields}) VALUES({values}) RETURNING *"
        cursor = self.connection.cursor()
        cursor.execute(query, params)

        return dict(cursor.fetchone())