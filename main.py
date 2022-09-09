from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from dal import create_flight, get_flights
from db import get_db
from schemas import CreateFlightRequest, FlightResponse

app = FastAPI()


@app.post("/flights", response_model=FlightResponse)
async def create_flight_view(
    request_data: CreateFlightRequest, session: AsyncSession = Depends(get_db)
):
    return await create_flight(session, request_data)


@app.get("/flights", response_model=list[FlightResponse])
async def get_flights_view(session: AsyncSession = Depends(get_db)):
    return await get_flights(session)
