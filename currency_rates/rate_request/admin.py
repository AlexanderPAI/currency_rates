from django.contrib import admin
from rate_request.models import RateRequest


class RateRequestAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'request_date',
        'currency_code',
        'target_currency_code',
        'rate',
    )
    search_fields = ('currency_code', 'target_currency_code')


admin.site.register(RateRequest, RateRequestAdmin)
