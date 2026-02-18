FROM python:3.12

WORKDIR /app

COPY uv.lock pyproject.toml ./
RUN uv sync --no-dev --no-cache

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
