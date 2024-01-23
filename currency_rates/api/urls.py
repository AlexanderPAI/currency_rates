from django.urls import path
from api.views import get_current_usd


# router = routers.DefaultRouter()
# router.register('/', RateRequestViewSet)

urlpatterns = [
    path('get-current-usd/', get_current_usd)
]
