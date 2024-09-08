from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny

from houses.serializers.api import tariffs as tariffs_s
from .mixins import ReadOrCreateViewSet
from ..models.tariffs import WaterMeter


@extend_schema_view(
    list=extend_schema(
        summary='Получить показания счетчиков воды', tags=['Счетчики воды']
    ),
    create=extend_schema(
        summary='Внести показания счетчика вода', tags=['Счетчики воды']
    ),
    retrieve=extend_schema(
        summary='Получить показания счетчика воды по id', tags=['Счетчики воды']
    ),
)
class WaterMeterViewSet(ReadOrCreateViewSet):
    """Вьюсет счетчика."""

    queryset = WaterMeter.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = tariffs_s.WaterMeterSerializer
