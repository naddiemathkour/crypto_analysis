from pprint import pp
import requests

while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    tradable_asset_pairs = requests.get('https://api.kraken.com/0/public/AssetPairs?pair='+primary_pairing+secondary_pairing)
    pp(tradable_asset_pairs.json())