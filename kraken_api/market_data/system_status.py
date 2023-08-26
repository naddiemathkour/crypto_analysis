from pprint import pp
import requests

system_status = requests.get('https://api.kraken.com/0/public/SystemStatus')

pp(system_status.json())