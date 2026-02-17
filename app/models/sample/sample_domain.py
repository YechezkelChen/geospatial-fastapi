from datetime import datetime

from pydantic import BaseModel


class SampleDomain(BaseModel):
    id: str | None = None
    latitude: float
    longitude: float
    signal_strength: float
    timestamp: datetime
