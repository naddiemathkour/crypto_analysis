from twilio.rest import Client
import dotenv

account_sid = dotenv.dotenv_values(dotenv.find_dotenv())['TWILIO_ACC_SID']
auth_token = dotenv.dotenv_values(dotenv.find_dotenv())['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_message(payload):
    return client.messages.create(body=payload, from_='+18883114089', to='2167736688')

