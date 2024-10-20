from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# The phone number you want to add as an outgoing caller ID
phone_number = '+1234567890'  # Replace with the desired phone number

# Make an HTTP POST request to add the outgoing caller ID
try:
    outgoing_caller_id = client \
        .outgoing_caller_ids \
        .create(phone_number)

    print(f'Outgoing Caller ID {outgoing_caller_id.phone_number} added successfully.')

except Exception as e:
    print(f'Error: {e}')
