import os
from datetime import datetime
from pathlib import Path

from api.serializers import RateRequestSerializer
from api.services.get_usd_from_api import get_currency_rate
from dotenv import load_dotenv
from rate_request.models import RateRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

env_file = Path(__file__).parent.parent / 'currency_rates' / '.env'
load_dotenv(env_file)

# Константы для запроса по api на https://openexchangerates.org
ENDPOINT = 'https://openexchangerates.org/api/latest.json'
API_ID = os.getenv('API_ID')


@api_view(http_method_names=['GET'],)
def get_current_usd(request):
    """
    Курс доллара США с отображением 10 последних запросов.
    """
    currency = 'USD'
    target_currency = 'RUB'
    currency_rate = get_currency_rate(
        ENDPOINT, API_ID, currency, target_currency
    )
    if currency_rate is not None:
        rate_request = RateRequest.objects.create(
            request_date=datetime.fromtimestamp(currency_rate['timestamp']),
            currency_code=currency,
            target_currency_code=target_currency,
            rate=currency_rate['rates'][target_currency]
        )
        serializer = RateRequestSerializer(rate_request)
        return Response(serializer.data)
    return Response(
        {'message': 'unable to get a response from the external api'}
    )
