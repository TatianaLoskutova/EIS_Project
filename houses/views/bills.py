from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework.views import APIView

from houses.tasks import calculation_rent


@extend_schema_view(
    post=extend_schema(
        summary='Расчет кварплаты дома', tags=['Расчет кварплаты']
    ),
)
class BillingView(APIView):
    """
    APIView  расчета квартплаты. Запись ее в БД.
    """

    def post(self, request, *args, **kwargs):
        calculation_rent.delay(self.kwargs.get('house_id'),
                               self.kwargs.get('month'))
        return Response({'message': 'Расчет квартплаты запущен!'})
