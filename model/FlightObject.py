from dataclasses import dataclass



@dataclass()
class FlightObject:
    ID:int
    AIRLINE_ID:int
    FLIGHT_NUMBER:int
    TAIL_NUMBER:str
    ORIGIN_AIRPORT_ID:int
    DESTINATION_AIRPORT_ID:int
    SCHEDULED_DEPARTURE_DATE:str
    DEPARTURE_DELAY:float
    ELAPSED_TIME:float
    DISTANCE:int
    ARRIVAL_DATE:str
    ARRIVAL_DELAY:int

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return f"{self.ID}-{self.AIRLINE_ID}-{self.FLIGHT_NUMBER}-{self.ORIGIN_AIRPORT_ID}-{self.DESTINATION_AIRPORT_ID}"

    def __hash__(self):
        return hash(self.ID)