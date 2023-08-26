from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    ohlc_data = requests.get('https://api.kraken.com/0/public/OHLC?pair='+primary_pairing+secondary_pairing+'&interval=60')
    pp(ohlc_data.json())