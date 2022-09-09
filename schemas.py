from datetime import datetime

from pydantic import BaseModel


class AirportResponse(BaseModel):
    id: int
    iata: str
    city: str
    state: str

    class Config:
        orm_mode = True


class FlightResponse(BaseModel):
    id: int
    code: str
    origin: AirportResponse
    departure_time: datetime
    destination: AirportResponse
    landing_time: datetime

    class Config:
        orm_mode = True


class CreateFlightRequest(BaseModel):
    code: str
    origin_id: int
    departure_time: datetime
    destination_id: int
    landing_time: datetime
