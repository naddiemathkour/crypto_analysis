from pprint import pp
import requests

relevant_tokens = ['ADA', 'DOT', 'SOL', 'ETH']
status_resp = requests.get('https://api.kraken.com/0/public/Assets')
coin_status = status_resp.json()['result']

ticker_info_resp = []
for token in relevant_tokens:
    ticker_info_resp.append(requests.get('https://api.kraken.com/0/public/Ticker?pair='+token+'USD').json()['result'])



for pair in ticker_info_resp:
    pp(pair)
    #print(list(pair.keys()), values['p'])

#for key in coin_status:
#    if relevant_tokens.__contains__(key):
#        print(coin_status[key]['altname'] + ': ' + coin_status[key]['status'])