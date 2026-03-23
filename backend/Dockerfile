FROM python:3.12-slim

# Install system dependencies needed by psycopg2-binary and asyncpg
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the files needed to install dependencies first (layer caching)
COPY pyproject.toml ./

# Install the package dependencies (no dev extras)
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir .

# Copy the rest of the source code
COPY src/ ./src/
COPY alembic/ ./alembic/

# Create a non-root user and hand ownership over
RUN useradd --create-home --shell /bin/bash appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

# Run Alembic migrations then start uvicorn
CMD alembic upgrade head && \
    uvicorn agentlens_api.main:app \
        --host 0.0.0.0 \
        --port 8080 \
        --workers 2
