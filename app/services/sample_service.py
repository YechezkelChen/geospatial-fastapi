import json
from datetime import datetime

from app.models.sample.sample_domain import SampleDomain
from app.repositories.sample_repository import SampleRepository
from app.schemas.sample_schema import SampleCreateRequest, SampleFilterRequest, SampleResponse


class SampleService:

    @staticmethod
    async def create_sample(sample_request: SampleCreateRequest) -> str:
        sample_domain = SampleDomain(
            latitude=sample_request.latitude,
            longitude=sample_request.longitude,
            signal_strength=sample_request.signal_strength,
            timestamp=sample_request.timestamp
        )
        return await SampleRepository.insert_sample(sample_domain)

    @staticmethod
    async def get_samples(polygon: str, start_time: datetime | None, end_time: datetime | None) -> list[SampleResponse]:
        polygon_coordinates = json.loads(polygon)

        samples = await SampleRepository.get_samples_in_polygon(
            polygon_coordinates=polygon_coordinates,
            start_time=start_time,
            end_time=end_time
        )

        return [SampleResponse(**sample.dict()) for sample in samples]
