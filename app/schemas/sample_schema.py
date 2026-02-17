from datetime import datetime

from pydantic import BaseModel


class SampleCreateRequest(BaseModel):
    latitude: float
    longitude: float
    signal_strength: float
    timestamp: datetime


class PolygonFilter(BaseModel):
    coordinates: list[list[float]]  # [[lon, lat], ...]


class SampleFilterRequest(BaseModel):
    polygon: PolygonFilter
    start_time: datetime | None = None
    end_time: datetime | None = None


class SampleResponse(BaseModel):
    id: str
    latitude: float
    longitude: float
    signal_strength: float
    timestamp: datetime
