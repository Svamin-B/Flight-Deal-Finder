import requests
from twilio.rest import Client
import smtplib

class NotificationManager:
    def send_message(self, price, destination, destination_airport, leave_date, return_date):
        client = Client(SID, AUTHTOK)
        message = client.messages.create(
                body=f"Only £{price} to fly from London-STN to {destination}-{destination_airport} from {leave_date} to {return_date}",
                from_='+18304606191',
                to=my_phone
        )

    def email(self, price, destination, destination_airport, leave_date, return_date, link):
        response = requests.get(url="https://api.sheety.co/9e5064469394e1ac656095c46c46c847/flightDeals/users")
        data = response.json()
        for item in data["users"]:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=(f"Subject:New Low Price Flight!\n\nOnly £{price} to fly from London-STN to {destination}-{destination_airport} from {leave_date} to {return_date}\n{link}").encode('utf-8'))

