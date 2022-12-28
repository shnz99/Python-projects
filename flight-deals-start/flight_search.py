import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://api.tequila.kiwi.com/"
        self.api_key = os.environ.get("TEQUILA_KEY")
        self.headers = {"apikey": self.api_key}

    def flightSearch(self, city):
        location_endpoint = f"{self.endpoint}locations/query"
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
