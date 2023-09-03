from twilio.rest import Client
import dotenv

account_sid = dotenv.dotenv_values(dotenv.find_dotenv())['TWILIO_ACC_SID']
auth_token = dotenv.dotenv_values(dotenv.find_dotenv())['TWILIO_AUTH_TOKEN']
send_to = dotenv.dotenv_values(dotenv.find_dotenv())['SEND_TO']

client = Client(account_sid, auth_token)

def send_message(payload):
    tokens = sorted(list(payload['tokens'].keys()))
    tokens.remove('USD.HOLD')
    message_append = '{coin}: {balance}\n'
    message = 'Weekly purchase executed. Token balances:\n'
    for token in tokens:
        message += message_append.format(coin=token, balance=payload['tokens'].pop(token))
    message += message_append.format(coin='Cost of current batch', balance=payload.pop('costs'))
    message += 'Portfolio Balance: ' + payload['portfolio_balance']
    return client.messages.create(body=message, from_='+18883114089', to=send_to)