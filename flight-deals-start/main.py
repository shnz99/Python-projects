# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.doc_connect()

for city in sheet_data:
    city["iataCode"] = flight_search.flightSearch(city["city"])

print(sheet_data)
