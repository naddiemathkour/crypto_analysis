from dotenv import dotenv_values
import os

import time
import urllib.parse
import hashlib
import hmac
import base64

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

data = {
    'nonce': time.time()
}

secrets = dotenv_values("./kraken_api/0/private/.env")
signature = get_kraken_signature(secrets['API_KEY'], data, secrets['API_SECRET'])

print('API-Sign: {}'.format(signature))