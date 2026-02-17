from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from app.api.v1.sample_routes import router as sample_router
from app.repositories.sample_repository import SampleRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    await SampleRepository.create_indexes()
    yield
    print("App is shutting down...")


app = FastAPI(title="Geospatial Signal API", lifespan=lifespan)
app.include_router(sample_router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
