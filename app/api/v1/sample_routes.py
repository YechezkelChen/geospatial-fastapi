from datetime import datetime

from fastapi import APIRouter

from app.schemas.sample_schema import SampleCreateRequest, SampleFilterRequest, SampleResponse
from app.services.sample_service import SampleService

router = APIRouter(prefix="/samples", tags=["Samples"])


@router.post("/", response_model=dict)
async def create_sample(sample: SampleCreateRequest):
    sample_id = await SampleService.create_sample(sample)
    return {"id": sample_id}


@router.get("/", response_model=list[SampleResponse])
async def get_samples(polygon: str, start_time: datetime | None = None, end_time: datetime | None = None):
    return await SampleService.get_samples(polygon, start_time, end_time)
