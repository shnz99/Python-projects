import os
import requests
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://api.tequila.kiwi.com"
        self.api_key = os.environ.get("TEQUILA_KEY")
        self.headers = {"apikey": self.api_key}
        self.today = datetime.today().strftime("%d/%m/%Y")
        self.date_to = (datetime.today() + timedelta(weeks=24)).strftime("%d/%m/%Y")

    def locationSearch(self, city):
        location_endpoint = f"{self.endpoint}/locations/query"
        data = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(
            url=location_endpoint, headers=self.headers, params=data
        )
        output = response.json()
        print(output)
        return output["locations"][0]["code"]

    def flightSearch(self, cityCode):
        search_endpoint = f"{self.endpoint}/v2/search"
        query = {
            "fly_from": f"city:LON",
            "fly_to": cityCode,
            "date_from": self.today,
            "date_to": self.date_to,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=search_endpoint, headers=self.headers, params=query)
        try:
            return response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {cityCode}.")
            return None
