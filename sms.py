# Download the helper library from https://www.twilio.com/docs/python/install
import keys
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
                     body="Fire alert.",
                     from_=keys.twilio_num,
                     to=keys.target_num
                 )

print(message.body)
