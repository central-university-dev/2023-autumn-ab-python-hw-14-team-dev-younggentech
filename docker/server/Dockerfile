# Use an official Python runtime as a parent image
FROM python:3.10 AS builder

# Set work directory
WORKDIR /opt/build

# Install Poetry
RUN pip install poetry

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock src ./

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Start final image
FROM python:3.10-slim

WORKDIR /opt/app

# Copy only the relevant files from the builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY src /opt/app/src

# Application entrypoint
CMD ["uvicorn", "src.homework.asgi:app", "--host", "0.0.0.0", "--port", "8000"]
