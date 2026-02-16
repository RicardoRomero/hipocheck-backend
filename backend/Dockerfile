FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --disable-pip-version-check --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "yourproject.wsgi:application"]
