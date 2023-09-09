CREATE TABLE kraken_data(
txid varchar(25) PRIMARY KEY,
userref int,
timestamp timestamp,
pair varchar(10),
ordertype varchar(4),
order_string varchar(50),
status varchar(10),
tok_price float,
volume float,
fee float,
total_cost float
);