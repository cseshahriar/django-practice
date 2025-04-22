import os
from twilio.rest import Client
from settings.local_settings import ( 
    TWILIO_ACCOUNT_SID, 
    TWILIO_AUTH_TOKEN, 
    TWILIO_NUMBER
)

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
twilio_number = TWILIO_NUMBER

# client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    # messages = client.messages.create(
    #     body=f'Hi! Your user and verification code is {user_code}',
    #     from_=twilio_number,
    #     to=f'{phone_number}'
    # )
    # print(messages)
    pass

