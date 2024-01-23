import os

from dotenv import load_dotenv
from json import loads
from pathlib import Path
from requests import get


def get_currency_rate(endpoint: str, app_id: str, currency: str, target_currency: str) -> dict or None:
    """Функция для запроса курса валюты с https://openexchangerates.org"""
    rate_request = f'{endpoint}?app_id={app_id}&base={currency}&symbols={target_currency}'
    response = get(rate_request)
    if response.status_code == 200:
        return loads(get(rate_request).text)
    return None
