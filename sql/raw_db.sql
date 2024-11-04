CREATE TABLE stock (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  symbol VARCHAR(100)
);

CREATE TABLE stock_record_price(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  stock_id INTEGER,
  stock_price FLOAT,
  date_price DATE,
  FOREIGN KEY (stock_id) REFERENCES stock(id)
);

CREATE TABLE portfolio(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  portfolio_name VARCHAR(100)
);

CREATE TABLE portfolio_stocks(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  portfolio_id INTEGER,
  stock_id INTEGER,
  date_join DATE,
  FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
  FOREIGN KEY (stock_id) REFERENCES stock(id)
);