from kraken_api.executions import executions
from pprint import pp

asset_volume_pairs = {'ADAUSD':'228.1', 'DOTUSD': '11.72', 'SOLUSD': '1.7782', 'XETHZUSD': '.043'} #Volume ammounts based on weekly buy

def main():
    for pair, volume in asset_volume_pairs.items():
        pp(executions.execute_order(pair, volume))

    print((executions.get_text_payload()))


if __name__ == '__main__':
    main()