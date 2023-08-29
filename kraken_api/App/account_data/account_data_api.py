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
    headers = {}
    headers['API-KEY'] = api_key
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)
    return requests.post((api_url + uri_path), headers=headers, data=data)

def get_account_balance():
    """
    Retrieve all cash balances, net of pending withdrawals.\n
    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call
    """
    return kraken_request('/0/private/Balance', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()
    print(resp)

def get_extended_account_balance():
    """
    Retrieve all extended account balances, including credits and held amounts.
    Balance available for trading is calculated as: available balance = balance + credit - credit_used - hold_trade.\n
    Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.\n
    API Key Permissions Required: Funds permissions: Query, Withdraw.
    """
    return kraken_request('/0/private/BalanceEx', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()

get_extended_account_balance()