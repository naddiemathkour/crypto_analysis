from endpoints.executions import executions
from endpoints.twilio import text_connection
from endpoints.database import database
from pprint import pp

asset_volume_pairs = {'ADAUSD':'114', 'DOTUSD': '5.86', 'SOLUSD': '.89', 'XETHZUSD': '.0215'} #Volume ammounts based on weekly buy

def main():
    
    userref = executions.get_userref() + 1

    #for pair, volume in asset_volume_pairs.items():
    #    pp(executions.execute_order(pair, volume, userref))
    
    #add new orders to database
    database.connect(executions.get_db_closed_orders())

    executions.get_closed_orders()

    #text_connection.send_message(executions.get_text_payload(userref))


if __name__ == '__main__':
    main()