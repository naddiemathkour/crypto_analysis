from pprint import pp
import requests

server_time = requests.get('https://api.kraken.com/0/public/Time')

pp(server_time.json())