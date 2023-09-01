import dotenv
import urllib.parse
import hashlib
import hmac
import base64

secrets = dotenv.dotenv_values(dotenv.find_dotenv())
api_url = 'https://api.kraken.com'
api_key = secrets['API_KEY_KRAKEN']
api_sec = secrets['API_SEC_KRAKEN']

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()
