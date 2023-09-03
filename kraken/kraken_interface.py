from endpoints.executions import executions
from endpoints.twilio import text_connection
from pprint import pp

asset_volume_pairs = {'ADAUSD':'228.1', 'DOTUSD': '11.72', 'SOLUSD': '1.7782', 'XETHZUSD': '.043'} #Volume ammounts based on weekly buy

def main():
    #for pair, volume in asset_volume_pairs.items():
    #    pp(executions.execute_order(pair, volume))

    #pp((executions.get_text_payload()))
    pp(text_connection.send_message(executions.get_text_payload()))
if __name__ == '__main__':
    main()