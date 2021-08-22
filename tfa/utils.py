import os
from twilio.rest import Client

account_sid = 'ACea3e56b5d026e200c5ba7aa9f127db3b'
auth_token = '2b5f19d9360ae512789a0323cdae1885'

client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    messages = client.messages.create(
        body=f'Hi! Your user and verification code is {user_code}',
        from_='+15622685529',
        to=f'{phone_number}'
    )
    print(messages)

