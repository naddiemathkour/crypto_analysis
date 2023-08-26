from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    pairing_resp = requests.get('https://api.kraken.com/0/public/Ticker?pair='+primary_pairing+secondary_pairing)
    pp(pairing_resp.json())