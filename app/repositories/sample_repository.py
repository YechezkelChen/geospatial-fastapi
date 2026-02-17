from datetime import datetime

from app.core.database import samples_collection
from app.models.sample.sample_domain import SampleDomain
from app.models.sample.sample_model import SampleModel


class SampleRepository:

    @staticmethod
    async def create_indexes():
        await samples_collection.create_index([("location", "2dsphere")])  # Create 2dsphere for geospatial queries
        await samples_collection.create_index("timestamp")

    @staticmethod
    async def insert_sample(sample: SampleDomain) -> str:
        sample_model = SampleModel(sample)
        result = await samples_collection.insert_one(sample_model.to_dict())
        return str(result.inserted_id)

    @staticmethod
    async def get_samples_in_polygon(polygon_coordinates: list[list[float]], start_time: datetime | None = None,
                                     end_time: datetime | None = None) -> list[SampleDomain]:
        query = {
            "location": {
                "$geoWithin": {
                    "$geometry": {
                        "type": "Polygon",
                        "coordinates": [polygon_coordinates],
                    }
                }
            }
        }

        if start_time or end_time:
            query["timestamp"] = {}
            if start_time:
                query["timestamp"]["$gte"] = start_time
            if end_time:
                query["timestamp"]["$lte"] = end_time

        docs = await samples_collection.find(query).to_list(length=None)

        return [SampleDomain(
            id=str(doc["_id"]),
            latitude=doc["location"]["coordinates"][1],
            longitude=doc["location"]["coordinates"][0],
            signal_strength=doc["signal_strength"],
            timestamp=doc["timestamp"]
        ) for doc in docs]
