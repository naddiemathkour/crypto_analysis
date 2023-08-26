from pprint import pp
import requests

tradable_assets = requests.get('https://api.kraken.com/0/public/AssetPairs').json()

def get_tradable_pairs(tradable_assets):

    return list(tradable_assets['result'].keys())

tradable_asset_list = get_tradable_pairs(tradable_assets)

"""
while True:
    primary_pairing = input('Enter primary pairing:\n')
    secondary_pairing = input('Enter secondary pairing:\n')
    tradable_asset_pairs = requests.get('https://api.kraken.com/0/public/AssetPairs?pair='+primary_pairing+secondary_pairing)
    pp(tradable_asset_pairs.json())
"""