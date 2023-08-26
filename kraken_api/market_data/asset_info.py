from pprint import pp
import requests

status_resp = requests.get('https://api.kraken.com/0/public/Assets')
asset_info = status_resp.json()['result']

while True:
    tokenSearch = input("Enter a token to search for:\n").upper()
    if tokenSearch in asset_info:
        pp(asset_info[tokenSearch])
    else: pp('Token not found.')