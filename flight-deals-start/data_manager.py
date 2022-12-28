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
            "https://api.sheety.co/e0c39ab4947543a4ce2ba49a5de8751b/flightDeals/prices"
        )

    def doc_connect(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        output = response.json()
        self.data = output["prices"]
        return self.data

    def update_doc(self):
        for city in self.data:
            new_data = {"price": {"iataCode": city["iataCode"]}}

            endpoint = f"{self.endpoint}/{city['id']}"
            response = requests.put(url=endpoint, json=new_data, headers=self.headers)
            print(response.text)
