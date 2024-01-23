import os

from dotenv import load_dotenv
from json import loads
from pathlib import Path
from requests import get


env_file = Path(__file__).parent.parent.parent / 'currency_rates' / '.env'
load_dotenv(env_file)


def get_currency_rate(endpoint: str, app_id: str, currency: str, target_currency: str) -> dict:
    """Функция для запроса курса валюты с https://openexchangerates.org"""
    rate_request = f'{endpoint}?app_id={app_id}&base={currency}&symbols={target_currency}'
    currency_rate = loads(get(rate_request).text)
    return currency_rate
