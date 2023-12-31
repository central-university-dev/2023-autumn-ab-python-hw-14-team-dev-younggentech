# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /opt/app

# Install Poetry
RUN pip install poetry

COPY Makefile /opt/app/

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock ./
COPY src ./src
COPY unit_tests ./unit_tests
COPY func_tests ./func_tests
# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install

# Application entrypoint
CMD ["uvicorn", "src.homework.asgi:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
