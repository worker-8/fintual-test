from .stock_repository import StockRepository
from .stock_record_price_repository import StockRecordPriceRepository
from .portfolio_repository import PortfolioRepository
from .portfolio_stocks_respository import PortfolioStockRepository

class UnitOfWork:
    def __init__(self, make_db_conn):
        self.connection = make_db_conn()

    def commit(self) -> None:
        self.connection.commit()

    def rollback(self) -> None:
        self.connection.rollback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with_rollback = True if exc_type is not None else False
        self._close(with_rollback)

    def _close(self, with_rollback: bool) -> None:
        if with_rollback:
            self.rollback()
        else:
            self.commit()

        self.connection.close()

    @property
    def stock_repository(self) -> StockRepository:
        return StockRepository(self.connection)
    
    @property
    def stock_record_price_repository(self) -> StockRecordPriceRepository:
        return StockRecordPriceRepository(self.connection)
    
    @property
    def portfolio_repository(self) -> PortfolioRepository:
        return PortfolioRepository(self.connection)
    
    @property
    def portfolio_stock_repository(self) -> PortfolioStockRepository:
        return PortfolioStockRepository(self.connection)