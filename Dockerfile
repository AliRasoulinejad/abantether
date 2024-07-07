# Stage 1: Build stage
FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root

COPY src/ ./

RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Command to start the server using Gunicorn
CMD ["gunicorn", "--workers=3", "--timeout=600", "--bind=0.0.0.0:8000", "config.wsgi:application"]
