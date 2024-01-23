import os

from datetime import datetime

from dotenv import load_dotenv
from pathlib import Path

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status

from rate_request.models import RateRequest
from api.serializers import RateRequestSerializer

from api.services.get_usd_from_api import get_currency_rate

env_file = Path(__file__).parent.parent / 'currency_rates' / '.env'
load_dotenv(env_file)

ENDPOINT = 'https://openexchangerates.org/api/latest.json'
API_ID = os.getenv('API_ID')


@api_view(
    http_method_names=['GET'],
)
def get_current_usd(request):
    currency = 'USD'
    target_currency = 'RUB'
    currency_rate = get_currency_rate(ENDPOINT, API_ID, currency, target_currency)
    if currency_rate is not None:
        history = RateRequest.objects.all()[:10]
        rate_request = RateRequest.objects.create(
            request_date=datetime.fromtimestamp(currency_rate['timestamp']),
            currency_code=currency,
            target_currency_code=target_currency,
            rate=currency_rate['rates'][target_currency]
        )
        serializer = RateRequestSerializer(rate_request)
        return Response(serializer.data)
    return Response({'message': 'unable to get a response from the external api'})
