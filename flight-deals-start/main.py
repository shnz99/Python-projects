# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.doc_connect()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.flightSearch(city["city"])

data_manager.data = sheet_data
data_manager.update_doc()
