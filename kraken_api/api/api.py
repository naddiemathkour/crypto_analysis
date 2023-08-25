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

keys = []
file = open('./kraken_api/0/private/new-api-key-test', 'r')
for line in file:
    keys.append(line)

signature = get_kraken_signature(keys[0], data, keys[1])

print('API-Sign: {}'.format(signature))