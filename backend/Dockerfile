FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy everything needed for install
COPY pyproject.toml ./
COPY src/ ./src/

# Install the package (includes dependencies)
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir .

# Copy Alembic files
COPY alembic/ ./alembic/
COPY alembic.ini ./

# Non-root user
RUN useradd --create-home --shell /bin/bash appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD alembic upgrade head && \
    uvicorn agentlenz_api.main:app \
        --host 0.0.0.0 \
        --port 8080 \
        --workers 2
