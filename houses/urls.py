from django.urls import include, path
from rest_framework.routers import DefaultRouter

from houses.views import bills, residences, tariffs

router = DefaultRouter()

router.register(r'houses', residences.HouseViewSet, basename='houses')
router.register(r'apartments', residences.ApartmentViewSet, basename='apartments')
router.register(r'watermeters', tariffs.WaterMeterViewSet, basename='water_meters')

urlpatterns = [
    path('', include(router.urls)),
    path(r'houses/<int:house_id>/month/<int:month>/',
         bills.BillingView.as_view(),
         name='bill'),
]
