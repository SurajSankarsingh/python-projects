from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '#twilio sid'
auth_token = '#twilion auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='#twilio number',
                    to=''
                )

print(message.sid)