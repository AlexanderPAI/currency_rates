from json import loads
from requests import get


def get_currency_rate(endpoint: str, app_id: str, currency: str, target_currency: str) -> dict or None:
    """
    Функция для запроса курса валюты по api с https://openexchangerates.org.
    Для возможности масштабизации при возникновении необходимости запроса курса иных валют,
    запрос выделен в отдельную функцию.
    Работоспособна только с указанным api, так как создана под структуру json-ответа именно с данного api.
    """
    rate_request = f'{endpoint}?app_id={app_id}&base={currency}&symbols={target_currency}'
    response = get(rate_request)
    if response.status_code == 200:
        return loads(get(rate_request).text)
    return None
