import requests
from pprint import pp

"""
Public Market Data api access points for Kraken.
Link to published documentation: https://docs.kraken.com/rest/#tag/Market-Data
"""

api_uri = 'https://api.kraken.com/0/public/'

def get_server_time():
    """
    Returns server time as a json object.
    Successful return: {'error': [], 'result': {'unixtime': 1693257175, 'rfc1123': 'Mon, 28 Aug 23 21:12:55 +0000'}}
    """
    resp = requests.get(api_uri + 'Time').json()
    print(resp)

def get_system_status():
    """
    Returns system status as a json object.
    Successful return: {'error': [], 'result': {'status': 'online', 'timestamp': '2023-08-28T21:17:31Z'}}
    """
    resp = requests.get(api_uri + 'SystemStatus').json()
    print(resp)

def get_asset_info():
    """
    Get information about the assets that are available for deposit, withdrawal, trading and staking.
    Successful return lists all assets on Kraken ecosystem in the following format:
    {'error': [], 'result': {
        '1INCH': {
            'aclass': 'currency', 'altname': '1INCH', 'decimals': 10, 'display_decimals': 5, 'status': 'enabled'}}
    
    Parameters:
    [optional] asset='Asset' => Comma delimited list of assets to get info (i.e. asset=XBT,ETH)
    [optional] aclass='AssetClass' => Asset class (defualt: currency)
    """
    resp = requests.get(api_uri + 'Assets').json()
    print(resp)

def get_tradable_asset_pairs():
    """
    Get tradable asset pairs.
    Successful return lists all asset pair combinations supported by Kraken. See documentation for returned format.
    
    Parameters:
    [optional] pair='AssetPair' => Asset pairs to get data for
    [optional] info='' (info(defualt): all info, leverage: leverage info, fees: fees scheduled, margin: margin info) => Info to retrieve
    """
    resp = requests.get(api_uri + 'AssetPairs').json()
    pp(resp)

def get_ticker_information():
    """
    Returns ticker's pricing information.
    Note: Today's prices start at midnight UTC.
    Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken. See documentation for returned format.

    Parameters:
    [optional] pair='AssetPair' => Asset pair to get data for (optional, default: all tradeable exchange pairs)
    """
    resp = requests.get(api_uri + 'Ticker?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)

def get_ohlc_data():
    """
    Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always 
    be present, regardless of the value of since.

    Parameters: 
    [required] pair='AssetPair' => Asset pair to get data for
    [optional] interval=(1 5 15 30 60 240 1440 10080 21600), default = 1 => Time frame interval in minutes
    [optional] since='UnixTimestamp' => Return up to 720 OHLC data points since given timestamp. Timestamp must be integer.
    """
    resp = requests.get(api_uri + 'OHLC?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)

def get_order_book():
    """

    
    Parameters:

    """

get_ohlc_data()
