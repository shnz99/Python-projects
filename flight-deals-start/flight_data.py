from datetime import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
        self,
        price,
        departure_airport_code,
        departure_city,
        cityCodeTo,
        cityTo,
        arrival,
        departure,
    ) -> None:
        self.price = price
        self.dac = departure_airport_code
        self.departure_city = departure_city
        self.cityCodeTo = cityCodeTo
        self.cityTo = cityTo
        self.arrival = arrival[:10]
        self.departure = departure[:10]

    def printingDetails(self):
        output = f"Low price Alert! Only {self.price}$ to fly from {self.dac}-{self.departure_city} to {self.cityCodeTo}-{self.cityTo}, from {self.arrival} to {self.departure}"
        return output
