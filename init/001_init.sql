-- Runs only the first time the data volume is created

DROP TABLE IF EXISTS terminal_data;

CREATE TABLE terminal_data (
  id serial PRIMARY KEY,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  terminal_id varchar NOT NULL DEFAULT 'NHFRKS50',
  cash_balance integer NOT NULL DEFAULT 0,
  days_until_load integer NOT NULL DEFAULT 31,
  last_transaction varchar UNIQUE
);

-- Optional: test row
-- INSERT INTO terminal_data (cash_balance, days_until_load, last_transaction)
-- VALUES (12000, 5, 'TXN001');

SELECT * FROM terminal_data;