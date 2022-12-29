import requests
import os
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data = {}
        self.sheety_token = os.environ.get("SHEETY_TOKEN")
        self.headers = {
            "Authorization": self.sheety_token,
        }
        self.endpoint = (
            "https://api.sheety.co/e0c39ab4947543a4ce2ba49a5de8751b/flightDeals"
        )

    def doc_connect(self):
        endpoint = f"{self.endpoint}/prices"
        response = requests.get(url=endpoint, headers=self.headers)
        output = response.json()
        self.data = output["prices"]
        return self.data

    def update_doc(self):
        for city in self.data:
            new_data = {"price": {"iataCode": city["iataCode"]}}

            endpoint = f"{self.endpoint}/prices/{city['id']}"
            response = requests.put(url=endpoint, json=new_data, headers=self.headers)
            print(response.text)

    def addNewUser(self):
        while True:
            print(
                "Welcome to Damian's Flight CLub.\nWe find the best flight deals and email you."
            )

            name = input("What is your first name?\n")
            last_name = input("What is your last name?\n")
            email = input("What is your email?\n")
            email2 = input("Type your email again.\n")
            if email == email2:
                print("You're in the club!")
                new_data = {
                    "user": {"firstName": name, "lastName": last_name, "email": email}
                }
                endpoint = f"{self.endpoint}/users"
                response = requests.post(
                    url=endpoint, json=new_data, headers=self.headers
                )
                break
            else:
                print("Error! Mismatched emails!")
