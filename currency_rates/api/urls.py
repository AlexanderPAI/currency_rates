from django.urls import include, path
from rest_framework import routers
from api.views import get_current_usd


# router = routers.DefaultRouter()
# router.register('/', RateRequestViewSet)

urlpatterns = [
    path('get-current-usd/', get_current_usd)
]
