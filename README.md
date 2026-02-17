# Geospatial Samples API

A **FastAPI** project in Python to handle geospatial signal data, stored in **MongoDB**, with endpoints to insert and query samples within polygons and optional time ranges.

---

### Features

- **Create sample:** Add a new geospatial sample (latitude, longitude, signal strength, timestamp).

- **Get samples:** Retrieve samples filtered by a polygon and optional time range.

- **MongoDB 2dsphere index** for fast geospatial queries.

- **3-layer architecture:**

    - **Model/Domain:** ```Sample``` data model

    - **Repository:** MongoDB operations

    - **Service:** Business logic

---

### Run

```docker-compose up --build```
