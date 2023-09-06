from twilio.rest import Client
import dotenv

message_header = dotenv.dotenv_values(dotenv.find_dotenv())

client = Client(message_header['TWILIO_ACC_SID'], message_header['TWILIO_AUTH_TOKEN'])

def send_message(message):
    print(message)
    return client.messages.create(body=message, from_=message_header['SEND_FROM'], to=message_header['SEND_TO'])