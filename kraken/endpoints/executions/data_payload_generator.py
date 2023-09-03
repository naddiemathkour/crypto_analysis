import time

def nonce():
    return str(int(1000 * time.time())) # without *1000, nonce may return the same value if generated within 1 second


def add_order_payload(pair, volume):
    return {
        'nonce': nonce(),
        'userref': 0,
        'ordertype': 'market',
        'type': 'buy',
        'volume': volume,
        'pair': pair,
        'validate': True #Remove after testing
    }


def get_nonce_dict():
    return {'nonce': nonce()}