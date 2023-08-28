import requests
import time
import dotenv
from api.kraken_signature import get_kraken_signature

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

resp = kraken_request('/0/private/OpenOrders', {
    "nonce": str(int(1000*time.time()))
}, api_key, api_sec)

print(resp.json())