"""
Private Trading api access points for Kraken.
Access to these functions requires a signature. This signature is aquired with accompanied and imported authorize_signature.py file.
Link to published REST API documentation: https://docs.kraken.com/rest/#tag/Trading

Review of online documentation is HIGHLY recommended for ALL functions. Implementation disregards many optional parameters in
function headers.
"""

import requests
import time
from ..kraken_signature.authorize_signature import *

def kraken_request(uri_path, data, api_key, api_sec):
    """
    Authenticated requests must include both API-Key and API-Sign HTTP headers, and nonce in the request payload.
    otp is also required in the payload if two-factor authentication (2FA) is enabled.\n
    Authenticated requests should be signed with the "API-Sign" header, using a signature generated with your private key, nonce, encoded payload, and URI path according to:
    Format: HMAC-SHA512 of (URI path + SHA256(nonce + POST data)) and base64 decoded secret API key
    """
    headers = {}
    headers['API-KEY'] = api_key
    headers['API-Sign'] = get_kraken_signature(uri_path, data, api_sec)
    return requests.post((api_url + uri_path), headers=headers, data=data)


def add_order(data):
    """
    Place a new order.
    Note: See the AssetPairs endpoint for details on the available trading pairs, 
    their price and quantity precisions, order minimums, available leverage, etc.

    REQUIRED Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] ordertype:string (enum: ['market', 'limit', 'stop-loss', 'take-profit', ... , 'settle-position]) => Order type.
    [required] type:string (enum: ['buy', 'sell']) => Order direction (buy/sell).
    [required] volume:string => Order quantity in terms of the base asset. Can be specified as 0 for closing margin orders to automatically fill the requisite quantity. This can only be used with limit order type.
    [required] pair:string => Asset pair 'id' or 'altname'. Format = <BaseCurrency><QuoteCurrency> e.g: ADAUSD

    Note: Please review the online documentation for optional Data Parameters.
    """
    return kraken_request('/0/private/AddOrder', data, api_key, api_sec).json()


def add_order_batch(data):
    """
    Send an array of orders (max: 15). Any orders rejected due to order validations, will be dropped and the rest of the batch is processed.
    All orders in batch should be limited to a single pair. The order of returned txid's in the response array is the same as the order of the order list sent in request.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] orders:Array of Order => See online documentation for details of Order parameters.
    [required] pair:string => Asset pair 'id' or 'altname'. Format = <BaseCurrency><QuoteCurrency> e.g: ADAUSD
    [optional] deadline:string => RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine should reject the new order request, in presence of latency or order queueing. min now() + 2 seconds, max now() + 60 seconds.
    [optional] validate:boolean (default: False) => Validate inputs only. Do not submit order.
    """
    return kraken_request('/0/private/AddOrderBatch', data, api_key, api_sec).json()


def edit_order(data):
    """
    Edit volume and price on open orders. Uneditable orders include triggered stop/profit orders,
    orders with conditional close terms attached, those already cancelled or filled,
    and those where the executed volume is greater than the newly supplied volume.
    post-only flag is not retained from original order after successful edit. post-only needs to be explicitly set on edit request.

    Required Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] txid:string|integer => Original Order ID or User Reference Id (userref) which is user-specified integer id used with the original order.
    If userref is not unique and was used with multiple order, edit request is denied with an error.
    [required] pair:string => Asset pair 'id' or 'altname'. Format = <BaseCurrency><QuoteCurrency> e.g: ADAUSD
    """
    return kraken_request('/0/private/EditOrder', data, api_key, api_sec).json()


def cancel_order(data):
    """
    Cancel a particular open order (or set of open orders) by txid or userref

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] txid:string|integer => Open order transaction ID (txid) or user reference (userref)
    """
    return kraken_request('/0/private/CancelOrder', data, api_key, api_sec).json()


def cancel_all_orders(data):
    """
    Cancel all open orders.

    Required Parameter:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    """
    return kraken_request('/0/private/CancelAll', data, api_key, api_sec).json()


def cancel_all_orders_after_x(data):
    """
    CancelAllOrdersAfter provides a "Dead Man's Switch" mechanism to protect the client from network malfunction,
    extreme latency or unexpected matching engine downtime. The client can send a request with a timeout (in seconds),
    that will start a countdown timer which will cancel all client orders when the timer expires.
    The client has to keep sending new requests to push back the trigger time, or deactivate the mechanism by specifying a timeout of 0.
    If the timer expires, all orders are cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.
    
    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] timeout:int => Duration (in seconds) to set/extend the timer by
    """
    return kraken_request('/0/private/CancelAllOrdersAfter', data, api_key, api_sec).json()


def cancel_order_batch(data):
    """
    Cancel multiple open orders by txid or userref (maximum 50 total unique IDs/references).

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] orders:Array of Order => See online documentation for details of Order parameters.
    """
    return kraken_request('/0/private/CancelOrderBatch', data, api_key, api_sec).json()