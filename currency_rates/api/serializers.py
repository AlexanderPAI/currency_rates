from rest_framework import serializers

from rate_request.models import RateRequest


class RateRequestSerializer(serializers.ModelSerializer):
    """Сериализатор запроса курса валюты."""
    # recent_requests = serializers.SerializerMethodField()

    class Meta:
        model = RateRequest
        fields = (
            'request_date',
            'currency_code',
            'target_currency_code',
            'rate',
            # 'recent_requests'
        )

    # def get_history(self, obj):
    #     pass


class AltSerializer(serializers.Serializer):
    """Test."""
    rate = RateRequestSerializer()

