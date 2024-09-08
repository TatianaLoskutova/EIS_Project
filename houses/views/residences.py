from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny

from houses.models.residences import Apartment, House
from houses.serializers.api.residences import ApartmentSerializer, HouseSerializer
from .mixins import ReadOrCreateViewSet


@extend_schema_view(
    list=extend_schema(
        summary='Получить список домов', tags=['Дома']
    ),
    create=extend_schema(
        summary='Внести дом', tags=['Дома']
    ),
    retrieve=extend_schema(
        summary='Получить дом по id', tags=['Дома']
    ),
)
class HouseViewSet(ReadOrCreateViewSet):
    """Вьюсет дома."""

    queryset = House.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = HouseSerializer


@extend_schema_view(
    list=extend_schema(
        summary='Получить список квартир', tags=['Квартиры']
    ),
    create=extend_schema(
        summary='Внести квартиру', tags=['Квартиры']
    ),
    retrieve=extend_schema(
        summary='Получить квартиру по id', tags=['Квартиры']
    ),
)
class ApartmentViewSet(ReadOrCreateViewSet):
    """Вьюсет квартиры."""

    queryset = Apartment.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ApartmentSerializer
