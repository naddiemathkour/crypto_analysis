from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    interval = input('Enter a time interval: (1, 5, 15, 30, 60)\n')
    ohlc_data = requests.get('https://api.kraken.com/0/public/OHLC?pair={0}&interval={1}'.format(primary_pairing+secondary_pairing, interval))
    pp(ohlc_data.json())