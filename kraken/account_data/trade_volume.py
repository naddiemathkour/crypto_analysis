import requests
import time
import dotenv
from api.kraken_signature import get_kraken_signature

from pprint import pp
"""
Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided. 
Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in fees and maker side in fees_maker. 
For pairs not on maker/taker, they will only be given in fees. 
Formatted as:
result": {
    "currency": "ZUSD",
    "volume": "200709587.4223",
    "fees": 
{
    "XXBTZUSD": 
    {
        "fee": "0.1000",
        "minfee": "0.1000",
        "maxfee": "0.2600",
        "nextfee": null,
        "nextvolume": null,
        "tiervolume": "10000000.0000"
    }
}
"""

secrets = dotenv.dotenv_values(dotenv.find_dotenv())
api_url = 'https://api.kraken.com'
api_key = secrets['API_KEY_KRAKEN']
api_sec = secrets['API_SEC_KRAKEN']

def kraken_request(uri_path, data, api_key, api_sec):
    headers = {}
    headers['API-Key'] = api_key
    # get_kraken_signature() as defined in the 'Authentication' section
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)             
    req = requests.post((api_url + uri_path), headers=headers, data=data)
    return req

resp = kraken_request('/0/private/TradeVolume?pair=DOTUSD', { #output doesn't make sense, investigate.
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

pp(resp.json())