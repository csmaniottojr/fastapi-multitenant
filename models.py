from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from base import Base


class Tenant(Base):
    __tablename__ = "tenant"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    subdomain = Column(String(100))


class Airport(Base):
    __tablename__ = "airport"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True)
    iata = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))


class Flight(Base):
    __tablename__ = "flight"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True)
    code = Column(String(100))
    origin_id = Column(Integer, ForeignKey("tenant.airport.id"))
    departure_time = Column(DateTime(timezone=True))
    destination_id = Column(Integer, ForeignKey("tenant.airport.id"))
    landing_time = Column(DateTime(timezone=True))

    origin = relationship("Airport", foreign_keys=[origin_id])
    destination = relationship("Airport", foreign_keys=[destination_id])
