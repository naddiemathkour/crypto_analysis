from account_data import *
from market_data import *

print(account_data_api.get_closed_orders())

print(market_data_api.get_asset_info()['result'].keys())
