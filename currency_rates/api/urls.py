from api.views import get_current_usd
from django.urls import path

# router = routers.DefaultRouter()
# router.register('/', RateRequestViewSet)

urlpatterns = [
    path('get-current-usd/', get_current_usd)
]
