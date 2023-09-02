from kraken_api import executions
from pprint import pp

asset_volume_pairs = {'ADAUSD':'228.1', 'DOTUSD': '11.72', 'SOLUSD': '1.7782', 'XETHZUSD': '.043'}

def main():
    executions.execute_buys(asset_volume_pairs)

if __name__ == '__main__':
    main()