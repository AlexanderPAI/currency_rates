from rest_framework import serializers

from rate_request.models import RateRequest


class RateRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса курса валюты."""

    class Meta:
        model = RateRequest
        fields = (
            'request_date',
            'currency_code',
            'target_currency_code',
            'rate',
        )
