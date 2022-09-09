from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Airport, Flight, Tenant
from schemas import CreateFlightRequest


async def create_flight(
    session: AsyncSession, request_data: CreateFlightRequest
) -> Flight:
    origin = await get_airport(session, request_data.origin_id)
    destination = await get_airport(session, request_data.destination_id)

    flight = Flight(
        code=request_data.code,
        origin=origin,
        destination=destination,
        departure_time=request_data.departure_time,
        landing_time=request_data.landing_time,
    )
    session.add(flight)
    await session.commit()
    return flight


async def get_airport(session: AsyncSession, airport_id: int) -> Airport | None:
    stmt = select(Airport).where(Airport.id == airport_id)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()


async def get_flights(session: AsyncSession) -> list[Flight]:
    stmt = select(Flight).options(
        selectinload(Flight.origin), selectinload(Flight.destination)
    )
    result = await session.execute(stmt)
    return result.scalars().fetchall()


async def get_tenant_by_subdomain(
    session: AsyncSession, subdomain: str
) -> Tenant | None:
    stmt = select(Tenant).where(Tenant.subdomain == subdomain)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()
