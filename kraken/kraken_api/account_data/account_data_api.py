"""
Private Account Data api access points for Kraken.
Access to these functions requires a signature. This signature is aquired with accompanied and imported authorize_signature.py file.
Link to published REST API documentation: https://docs.kraken.com/rest/#tag/Account-Data
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


def get_account_balance():
    """
    Retrieve all cash balances, net of pending withdrawals.\n

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    """
    return kraken_request('/0/private/Balance', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def get_extended_account_balance():
    """
    Retrieve all extended account balances, including credits and held amounts.
    Balance available for trading is calculated as: available balance = balance + credit - credit_used - hold_trade.\n

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.\n
    """
    return kraken_request('/0/private/BalanceEx', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def get_trade_balance(asset):
    """
    Retrieve a summary of collateral balances, margin position valuations, equity and margin level.
    Returned variables = {equivalent balance, trade balance, margin, unrealized net profit... see documentation for rest }

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] asset='ASSET' => Asset used to determine balance.
    """

    return kraken_request('/0/private/TradeBalance', {'nonce':str(int(1000*time.time())), 'asset':asset}, api_key, api_sec).json()


def get_open_orders():
    """
    Retrieve information about currently open orders.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    [optional] userref:int32 => Restrict results to given user reference id.
    """
    return kraken_request('/0/private/OpenOrders', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def get_closed_orders():
    """
    Retrieve information about orders that have been closed (filled or cancelled THROUGH KRAKEN PRO).
    50 results are returned at a time, the most recent by default.
    Note: If an order's tx ID is given for start or end time, the order's opening time (opentm) is used

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    [optional] userref:int32 => Restrict results to given user reference id.
    [optional] start:int => Starting unix timestamp or order tx ID of results (exclusive).
    [optional] end:int => Ending unix timestamp or order tx ID of results (inclusive).
    [optional] ofs:int => Result offset for pagination.
    [optional] closetime:string (default: 'both', enum: ['open', 'close', 'both']) => Which time to use in search.
    [optional] consolidate_taker:boolean (default: True) => Wheter or not to consolidate trades by individual taker trades.
    """
    return kraken_request('/0/private/ClosedOrders', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def query_orders_info(txid):
    """
    Retrieve information about specific orders.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    [optional] userref:int32 => Restrict results to given user reference id.
    [required] txid:string => Comma delimited list of transaction IDs to query info about (50 maximum).
    [optional] consolidate_taker:boolean (default: True) => Wheter or not to consolidate trades by individual taker trades.
    """
    return kraken_request('/0/private/QueryOrders', {'nonce':str(int(1000*time.time())), 'txid':txid}, api_key, api_sec).json()


def get_trades_history(data):
    """
    Retrieve information about trades/fills. 50 results are returned at a time, the most recent by default.

    Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the asset pair (pair_decimals and lot_decimals), not the individual assets' precision (decimals).

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] type:string (default: 'all', enum: ['all', 'any position', 'closed position', 'no position']) => Type of trade.
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    [optional] start:int => Starting unix timestamp or order tx ID of results (exclusive).
    [optional] end:int => Ending unix timestamp or order tx ID of results (inclusive).
    [optional] ofs:int => Result offset for pagination.
    [optional] consolidate_taker:boolean (default: True) => Wheter or not to consolidate trades by individual taker trades.
    """
    return kraken_request('/0/private/TradesHistory', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def query_trades_info(txid):
    """
    Retrieve information about specific trades/fills.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] txid:string => Comma delimited list of transaction IDs to query info about (50 maximum).
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    """
    return kraken_request('/0/private/QueryTrades', {'nonce':str(int(1000*time.time())), 'txid':txid}, api_key, api_sec).json()


def get_open_positions(data):
    """
    Get information about open margin positions.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] txid:string => Comma delimited list of transaction IDs to.
    [optional] docalcs:boolean (default: False) =>  Whether to include Profit and Loss (P&L) calculations.
    [optional] consolidation:string (value: 'market') => Consolidate positions by market/pair.
    """
    return kraken_request('/0/private/OpenPositions', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def get_ledgers_info(data):
    """
    Retrieve information about ledger entries. 50 results are returned at a time, the most recent by default.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] asset:string (default: 'all') => Comma delimited list of assets to restrict output to.
    [optional] aclass:string (default: 'currency') => Asset class.
    [optional] type:string (default: 'all', enum: ['all', 'deposit', 'withdrawl', 'trade', 'margin', 'rollover', 'credit', 'transfer',
    'settled', 'staking', 'sale']) => Type of ledger to retrieve.
    [optional] start:int => Starting unix timestamp or order tx ID of results (exclusive).
    [optional] end:int => Ending unix timestamp or order tx ID of results (inclusive).
    [optional] ofs:int => Result offset for pagination.
    [optional] without_count:boolean (defualt: False) => If true, does not retrieve count of ledger entries. Request can be noticeably faster for users with many ledger entries as this avoids an extra database query.
    """
    return kraken_request('/0/private/Ledgers', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def query_ledgers(data):
    """
    Retrieve information about specific ledger entries. 

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] id:string => Comma delimited list of ledger IDs to query info about (20 maximum).
    [optional] trades:boolean (default: False) => Whether or not to include trades related to position in output.
    """
    return kraken_request('/0/private/QueryLedgers', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def get_trade_volume():
    """
    Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided.
    Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in fees and maker side in fees_maker. For pairs not on maker/taker, they will only be given in fees.
    
    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [optional] pair:string => Comma delimited list of asset pairs to get fee info on.
    """
    return kraken_request('/0/private/TradeVolume', {'nonce':str(int(1000*time.time()))}, api_key, api_sec).json()


def request_export_report(data):
    """
    Request export of trades or ledgers.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] report:string (enum: ['trades', 'ledgers']) => Type of data to export.
    [optional] format:string (default: 'CSV', enum: ['CSV', 'TSV']) => File format to export.
    [required] description:string
    """
    return kraken_request('/0/private/AddExport', data, api_key, api_sec).json()


def get_export_report_status(data):
    """
    Get status of requested data exports.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] report:string (enum: ['trades', 'ledgers']) => Type of reports to inquire about.
    """
    return kraken_request('/0/private/ExportStatus', data, api_key, api_sec).json()


def retrieve_data_export(data):
    """
    Retrieve a processed data export.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] id:string => Report ID to retrieve.
    """
    return kraken_request('/0/private/RetrieveExport', data, api_key, api_sec).json()


def delete_export_report(data):
    """
    Delete exported trades/ledgers report.

    Data Parameters:
    [required] nonce:int32 => 'number once' must be a changing and incrementing number with each api call.
    [required] id:string => ID of report to delete or cancel.
    [required] type:string (enum: ['cancel', 'delete']) => delete can only be used for reports that have already been processed. Use cancel for queued or processing reports.
    """
    return kraken_request('/0/private/RemoveExport', data, api_key, api_sec).json()

#todo: function that generates data, function that generates nonce