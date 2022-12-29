# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

sheet_data = data_manager.doc_connect()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flightSearch.locationSearch(city["city"])

data_manager.data = sheet_data
data_manager.update_doc()

for city in sheet_data:
    flight_data = flightSearch.flightSearch(city["iataCode"])
    for data in flight_data[:1]:
        if data["price"] < city["lowestPrice"]:
            flightData = FlightData(
                price=data["price"],
                departure_airport_code=data["flyFrom"],
                departure_city=data["cityFrom"],
                cityCodeTo=data["cityCodeTo"],
                cityTo=data["cityTo"],
                arrival=data["utc_arrival"],
                departure=data["utc_departure"],
            )
            notificationManager.sendSms(flightData.printingDetails())
