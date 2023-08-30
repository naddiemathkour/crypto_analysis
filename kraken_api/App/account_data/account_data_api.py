import requests
import time
import dotenv

from signature.kraken_signature import get_kraken_signature

"""
Private Market Data api access points for Kraken.
Access to these functions requires a signature. This signature is aquired with accompanied kraken_signature.py file.
Link to published REST API documentation: https://docs.kraken.com/rest/#tag/Market-Data
"""

secrets = dotenv.dotenv_values(dotenv.find_dotenv())

api_key = secrets['API_KEY_KRAKEN']
api_sec = secrets['API_SEC_KRAKEN']
api_url = 'https://api.kraken.com'

def kraken_request(uri_path, data, api_key, api_sec):
    """
    Authenticated requests must include both API-Key and API-Sign HTTP headers, and nonce in the request payload.
    otp is also required in the payload if two-factor authentication (2FA) is enabled.\n
    Authenticated requests should be signed with the "API-Sign" header, using a signature generated with your private key, nonce, encoded payload, and URI path according to:
    Format: HMAC-SHA512 of (URI path + SHA256(nonce + POST data)) and base64 decoded secret API key
    """
    headers = {}
    headers['API-KEY'] = api_key
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)
    return requests.post((api_url + uri_path), headers=headers, data=data)

def get_account_balance():
    """
    Retrieve all cash balances, net of pending withdrawals.\n
    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    """
    return kraken_request('/0/private/Balance', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()

def get_extended_account_balance():
    """
    Retrieve all extended account balances, including credits and held amounts.
    Balance available for trading is calculated as: available balance = balance + credit - credit_used - hold_trade.\n
    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.\n
    """
    return kraken_request('/0/private/BalanceEx', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()

def get_trade_balance(asset):
    """
    Retrieve a summary of collateral balances, margin position valuations, equity and margin level.
    Returned variables = {equivalent balance, trade balance, margin, unrealized net profit... see documentation for rest }

    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] asset='ASSET' => Base asset used to determine balance.
    """

    return kraken_request('/0/private/TradeBalance', {'nonce':str(int(1000*time.time())), 'asset':asset}, api_key, api_sec).json()

def get_open_orders():
    """
    Retrieve information about currently open orders.

    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] trades:boolean (default: False)=> Whether or not to include trades related to position in output.
    [optional] userref:int32 => Restrict results to given user reference id.
    """
    return kraken_request('/0/private/OpenOrders', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()

def get_closed_orders():
    """
    Retrieve information about orders that have been closed (filled or cancelled).
    50 results are returned at a time, the most recent by default.
    Note: If an order's tx ID is given for start or end time, the order's opening time (opentm) is used

    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] trades:boolean (default: False)=> Whether or not to include trades related to position in output.
    [optional] userref:int32 => Restrict results to given user reference id.
    [optional] start:int => Starting unix timestamp or order tx ID of results (exclusive).
    [optional] end:int => Ending unix timestamp or order tx ID of results (inclusive).
    [optional] ofs:int => Result offset for pagination.
    [optional] closetime:string (default: 'both', ['open', 'close', 'both']) => Which time to use in search.
    [optional] consolidate_taker:boolean (default: True) => Wheter or not to consolidate trades by individual taker trades.
    """
    return kraken_request('/0/private/ClosedOrders', {'nonce':str(int(1000*time.time())), 'trades': True}, api_key, api_sec).json()

get_closed_orders() #Before moving on: try to get closed orders to print. Also an issue with relative importing from market_data_api.py