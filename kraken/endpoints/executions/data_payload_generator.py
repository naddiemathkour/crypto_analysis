import time

def nonce():
    return str(int(1000 * time.time())) # without *1000, nonce may return the same value if generated within 1 second


def add_order_payload(pair, volume, userref):
    return {
        'nonce': nonce(),
        'userref': userref,
        'ordertype': 'market',
        'type': 'buy',
        'volume': volume,
        'pair': pair,
        'validate': True #True = order testing, Flase = real order
    }


def recent_closed_order_payload(userref):
    return {
        'nonce': nonce(),
        'userref': userref
    }


def get_nonce_dict():
    return {'nonce': nonce()}