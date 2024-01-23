from rest_framework import serializers

from rate_request.models import RateRequest


class RateRequestListSerializer(serializers.ModelSerializer):
    """Сериализатор списка запросов курсов валют."""

    class Meta:
        model = RateRequest
        fields = (
            'request_date',
            'currency_code',
            'target_currency_code',
            'rate',
        )


class RateRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса текущего курса валюты с историей запросов."""
    recent_requests = serializers.SerializerMethodField()

    class Meta:
        model = RateRequest
        fields = (
            'request_date',
            'currency_code',
            'target_currency_code',
            'rate',
            'recent_requests',
        )

    def get_recent_requests(self, obj):
        data = RateRequest.objects.all()[:10]
        serializer = RateRequestListSerializer(data, many=True)
        return serializer.data
