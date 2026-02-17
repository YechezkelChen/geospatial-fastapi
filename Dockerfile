FROM python:3.12

WORKDIR /app

RUN pip install uv
RUN uv sync

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
