from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    recent_trades = requests.get('https://api.kraken.com/0/public/Trades?pair='+primary_pairing+secondary_pairing)
    pp(recent_trades.json())