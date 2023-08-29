import requests
from pprint import pp

"""
Public Market Data api access points for Kraken.
Link to published REST API documentation: https://docs.kraken.com/rest/#tag/Market-Data
"""

api_uri = 'https://api.kraken.com/0/public/'

def get_server_time():
    """
    Returns server time as a json object.
    Successful return: {'error': [], 'result': {'unixtime': 1693257175, 'rfc1123': 'Mon, 28 Aug 23 21:12:55 +0000'}}
    """
    return requests.get(api_uri + 'Time').json()
    print(resp)

def get_system_status():
    """
    Returns system status as a json object.
    Successful return: {'error': [], 'result': {'status': 'online', 'timestamp': '2023-08-28T21:17:31Z'}}
    """
    return requests.get(api_uri + 'SystemStatus').json()
    print(resp)

def get_asset_info():
    """
    Returns information about the assets that are available for deposit, withdrawal, trading and staking.
    Successful return lists all assets on Kraken ecosystem in the following format:
    {'error': [], 'result': {
        '1INCH': {
            'aclass': 'currency', 'altname': '1INCH', 'decimals': 10, 'display_decimals': 5, 'status': 'enabled'}}
    
    Parameters:\n
    [optional] asset='Asset' => Comma delimited list of assets to get info (i.e. asset=XBT,ETH)
    [optional] aclass='AssetClass' => Asset class (defualt: currency)
    """
    return requests.get(api_uri + 'Assets').json()
    print(resp)

def get_tradable_asset_pairs():
    """
    Returns tradable asset pairs.
    Successful return lists all asset pair combinations supported by Kraken. See documentation for returned format.
    
    Parameters:\n
    [optional] pair='ASSET_PAIR' => Asset pairs to get data for
    [optional] info='' (info(defualt): all info, leverage: leverage info, fees: fees scheduled, margin: margin info) => Info to retrieve
    """
    return requests.get(api_uri + 'AssetPairs').json()
    print(resp)

def get_ticker_information():
    """
    Returns ticker's pricing information.
    Note: Today's prices start at midnight UTC.
    Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken. See documentation for returned format.

    Parameters:\n
    [optional] pair='ASSET_PAIR' => Asset pair to get data for (optional, default: all tradeable exchange pairs)
    """
    return requests.get(api_uri + 'Ticker?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)

def get_ohlc_data():
    """
    Returns list of Open, High, Low, and Close prices for ASSET_PAIR
    Note: the 'last' entry in the OHLC array is for the current, not-yet-committed frame and will always 
    be present, regardless of the value of since.

    Parameters:\n 
    [required] pair='ASSET_PAIR' => Asset pair to get data for.\n
    [optional] interval:int=(1 5 15 30 60 240 1440 10080 21600), default = 1 => Time frame interval in minutes.\n
    [optional] since:int=UNIX_TIMESTAMP => Return up to 720 OHLC data points since given timestamp. Timestamp must be integer.
    """
    return requests.get(api_uri + 'OHLC?pair=' + 'ADAUSD&interval=60').json() #@@@@@ interval will be useful here
    print(resp)

def get_order_book():
    """
    Returns a Json object containing the asks and bids for the requested asset pair.

    Parameters:\n
    [required] pair='ASSET_PAIR' => Asset pair to get data for
    [optional] count:int=[1..500] (default: 100) => Maximum number of asks/bids
    """

    return requests.get(api_uri + 'Depth?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)

def get_recent_trades():
    """
    Returns the last 1000 trades by default.
    
    Parameters:\n
    [required] pair='ASSET_PAIR' => Asset pair to get data for
    [optional] since:int=UNIX_TIMESTAMP => Return trade data since given timestamp
    [optional] count:int=[1..1000] (default: 1000) => Return specific number of trades, up to 1000
    """
    return requests.get(api_uri + 'Trades?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)

def get_recent_spreads():
    """
    
    Parameters:\n
    [required] pair='ASSET_PAIR' => Asset pair to get data for
    [optional] since:int=UNIX_TIMESTAMP => Returns spread data since given timestamp.
                        Intended for incremental updates within available dataset (does not contain all historical spreads).
    """
    return requests.get(api_uri + 'Spread?pair=' + 'ADAUSD').json() #@@@@@
    print(resp)