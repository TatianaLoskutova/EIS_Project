from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny

from houses.models.residences import Apartment, House
from houses.serializers.api import residences as residences_s
from .mixins import ReadOrCreateViewSet


@extend_schema_view(
    get=extend_schema(
        summary='Получить список домов', tags=['Дома']
    ),
    post=extend_schema(
        summary='Внести дом', tags=['Дома']
    ),
)
class HouseViewSet(ReadOrCreateViewSet):
    """Вьюсет дома."""

    queryset = House.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = residences_s.HouseSerializer


@extend_schema_view(
    get=extend_schema(
        summary='Получить список квартир', tags=['Квартиры']
    ),
    post=extend_schema(
        summary='Внести квартиру', tags=['Квартиры']
    ),
)
class ApartmentViewSet(ReadOrCreateViewSet):
    """Вьюсет квартиры."""

    queryset = Apartment.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = residences_s.ApartmentSerializer
