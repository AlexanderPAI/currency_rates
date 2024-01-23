FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY /currency_rates /app
