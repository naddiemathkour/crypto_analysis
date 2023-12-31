import operator
import datetime

from ..executions import data_payload_generator
from ..trading import trading_api
from ..account_data import account_data_api
from pprint import pp

def get_userref() -> int:
    """
    Return the 'userref' value of the last closed trade.
    """
    closed_orders = account_data_api.get_closed_orders(data_payload_generator.get_nonce_dict())['result']['closed']
    values = list(closed_orders.values())[0]
    return operator.itemgetter('userref')(values)


def get_closed_orders():
    """
    Retrieve all closed orders
    """
    closed_orders = account_data_api.get_closed_orders(data_payload_generator.get_nonce_dict())['result']['closed']
    return closed_orders

def get_db_closed_orders() -> list:
    """
    Retrieves data from Kraken as list of dictionaries pre-formatted for PostgreSQL insertion.

    Parameter:
    userref (int) => used to retrieve group of orders.
    """

    closed_orders = account_data_api.get_closed_orders(data_payload_generator.get_nonce_dict())['result']['closed']
    txid_list = list(closed_orders)
    order_details = list(closed_orders.values())

    data_to_save = []

    for i in range(0, len(txid_list)):
        curr_order = order_details[i]
        order_description = operator.itemgetter('descr')(curr_order)

        tok_price = float(operator.itemgetter('price')(curr_order))
        volume = float(operator.itemgetter('vol_exec')(curr_order))
        fee = float(operator.itemgetter('fee')(curr_order))
        date_time = datetime.datetime.fromtimestamp(operator.itemgetter('closetm')(curr_order)).replace(microsecond=0)

        data_to_save.append({
            'txid': txid_list[i],
            'userref': operator.itemgetter('userref')(curr_order),
            'timestamp': date_time.isoformat(sep=' ', timespec='auto'),
            'pair': operator.itemgetter('pair')(order_description),
            'order_type': operator.itemgetter('type')(order_description),
            'order': operator.itemgetter('order')(order_description),
            'status': operator.itemgetter('status')(curr_order),
            'tok_price': tok_price,
            'volume': volume,
            'fee': fee,
            'total_cost': tok_price * volume + fee,
        })
    return list(data_to_save)


def execute_order(pair, volume, userref):
    """
    Execute Buy order.

    Parameters:
    pair (string) => Purchasing pair (i.e. ADAUSD).
    volume (int) => Amount of primary token to be purchased.
    userref (int) => Number used to group batches of orders together.
    """
    return trading_api.add_order(data_payload_generator.add_order_payload(pair, volume, userref))


def fetch_data():
    """
    Build PSQL statment to fetch information from database.
    """



def get_text_payload(userref) -> str:
    """
    Retrieves token and cost data. Returns a string formatted for Twilio text notification.
    """
    cost_to_buy = 0
    token_balances = account_data_api.get_account_balance(data_payload_generator.get_nonce_dict())['result']
    portfolio_balance = account_data_api.get_trade_balance(data_payload_generator.get_nonce_dict())['result']['eb']
    
    recent_orders = list(
        account_data_api.get_closed_orders(data_payload_generator.recent_closed_order_payload(userref))['result']['closed'].values()
    )

    #sum cost of each recent transaction
    for order in recent_orders:
        cost_to_buy += float(order.pop('cost'))

    #sort token list and remove USD.HOLD for consistant result
    tokens = sorted(list(token_balances.keys()))
    tokens.remove('USD.HOLD')

    #instantiate message
    message_append = '{coin}: {balance}\n'
    message = 'Weekly purchase executed. Token balances:\n'

    for token in tokens:
        message += message_append.format(coin=token, balance=str(token_balances.pop(token)))
    
    message += message_append.format(coin='Cost of current batch', balance=str(round(cost_to_buy, 2)))
    message += 'Portfolio Balance: ' + portfolio_balance

    return message
    