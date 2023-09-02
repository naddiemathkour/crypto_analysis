import time

def get_nonce():
    return str(int(time.time() * 1000)) # without *1000, nonce may return the same value if generated within 1 second


def market_buy_payload(pair, volume):
    return {
        'nonce': get_nonce(),
        'userref': 0,
        'ordertype': 'market',
        'type': 'buy',
        'volume': volume,
        'pair': pair,
        'validate': True #Remove after testing
    }