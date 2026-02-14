FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install -r requirements.txt --no-cache-dir && \
    /opt/venv/bin/python -m django collectstatic --no-input

COPY . .

CMD ["/opt/venv/bin/gunicorn", "hipocheckca.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3"]

