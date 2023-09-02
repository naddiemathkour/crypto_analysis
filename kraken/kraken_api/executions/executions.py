from ..executions import data_payload_generator
from ..trading import trading_api
from pprint import pp

def execute_buys(asset_volume_pairs):
    for pair, volume in asset_volume_pairs.items():
        pp(trading_api.add_order(data_payload_generator.market_buy_payload(pair, volume)))