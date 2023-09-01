import requests
import time
from ..kraken_signature.authorize_signature import *

"""
Private Funding api access points for Kraken.
Access to these functions requires a signature. This signature is aquired with accompanied and imported authorize_signature.py file.
Link to published REST API documentation: https://docs.kraken.com/rest/#tag/Funding
"""

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

def get_deposit_methods():
    """
    Retrieve methods available for depositing a particular asset.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] asset:string => Asset being deposited.
    """
    return kraken_request('/0/private/DepositMethods', {'nonce':str(int(1000*time.time())), 'asset':'USD'}, api_key, api_sec).json()
