import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def sendSms(self, output):
        acc_sid = os.environ.get("TWILIO_SID")
        acc_auth = os.environ.get("TWILIO_AUTH")
        your_num = os.environ.get("YOUR_NUMBER")
        from_num = os.environ.get("TWILIO_NUMBER")

        client = Client(acc_sid, acc_auth)
        message = client.messages.create(body=output, from_=from_num, to=your_num)
        print(message.status)
