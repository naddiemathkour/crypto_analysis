from ..executions import data_payload_generator
from ..trading import trading_api
from ..account_data import account_data_api
from pprint import pp

def execute_order(pair, volume):
    return trading_api.add_order(data_payload_generator.add_order_payload(pair, volume))

def get_text_payload():
    token_balances = account_data_api.get_account_balance(data_payload_generator.get_nonce_dict())['result']
    portfolio_balance = account_data_api.get_trade_balance(data_payload_generator.get_nonce_dict())['result']['eb']
    return {
        'tokens': token_balances,
        'portfolio_balance': portfolio_balance
    }
    