import os
from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    messages = client.messages.create(
        body=f'Hi! Your user and verification code is {user_code}',
        from_='+15622685529',
        to=f'{phone_number}'
    )
    print(messages)

