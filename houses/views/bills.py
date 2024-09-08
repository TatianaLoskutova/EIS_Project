from rest_framework.response import Response
from rest_framework.views import APIView

from houses.tasks import calculation_rent


class BillingView(APIView):
    """
    APIView  расчета квартплаты. Запись ее в БД.
    """

    def get(self, request, *args, **kwargs):
        calculation_rent.delay(self.kwargs.get('house_id'),
                               self.kwargs.get('month'))
        return Response({'message': 'Расчет квартплаты запущен!'})
