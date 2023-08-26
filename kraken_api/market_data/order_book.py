from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    order_book = requests.get('https://api.kraken.com/0/public/Depth?pair='+primary_pairing+secondary_pairing)
    pp(order_book.json())