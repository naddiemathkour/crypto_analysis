from ..executions import data_payload_generator
from ..trading import trading_api
from ..account_data import account_data_api
from pprint import pp

def get_userref():
    closed_orders = account_data_api.get_closed_orders(data_payload_generator.get_nonce_dict())['result']['closed']
    values = list(closed_orders.values())[0]
    return values.pop('userref')


def execute_order(pair, volume, userref):
    return trading_api.add_order(data_payload_generator.add_order_payload(pair, volume, userref))


def get_text_payload(userref):
    cost_to_buy = 0
    token_balances = account_data_api.get_account_balance(data_payload_generator.get_nonce_dict())['result']
    portfolio_balance = account_data_api.get_trade_balance(data_payload_generator.get_nonce_dict())['result']['eb']
    
    recent_orders = list(
        account_data_api.get_closed_orders(data_payload_generator.recent_closed_order_payload(userref))['result']['closed'].values()
    )

    for order in recent_orders:
        cost_to_buy += float(order.pop('cost'))

    tokens = sorted(list(token_balances.keys()))
    tokens.remove('USD.HOLD')

    message_append = '{coin}: {balance}\n'
    message = 'Weekly purchase executed. Token balances:\n'

    for token in tokens:
        message += message_append.format(coin=token, balance=str(token_balances.pop(token)))
    
    message += message_append.format(coin='Cost of current batch', balance=str(round(cost_to_buy, 2)))
    message += 'Portfolio Balance: ' + portfolio_balance

    return message
    