import requests
import time
import dotenv
from api.kraken_signature import get_kraken_signature

from pprint import pp
"""
Retrieve information about specific ledger entries. Formatted as:
"result": {
    "L4UESK-KG3EQ-UFO4T5": 
{
    "refid": "TJKLXF-PGMUI-4NTLXU",
    "time": 1688464484.1787,
    "type": "trade",
    "subtype": "",
    "aclass": "currency",
    "asset": "ZGBP",
    "amount": "-24.5000",
    "fee": "0.0490",
    "balance": "459567.9171"
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

resp = kraken_request('/0/private/QueryLedgers', { #not working as of now, investigate later if functionality is essential
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

pp(resp.json())