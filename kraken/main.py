from kraken_api import account_data_api, market_data_api, trading_api, funding_api

order_id = 'ORTNKC-VWAAM-6TJQPC'
txid = 'TUCYVF-ZCWL4-EV2F57'

print(account_data_api.get_account_balance())