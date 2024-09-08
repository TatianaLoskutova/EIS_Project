from datetime import date

from celery import shared_task
from django.db.models import F, OuterRef, Subquery, Sum

from .models.residences import Apartment
from .models.tariffs import WaterMeter
from .service import add_bill_in_db


@shared_task(name='calculation_bills')
def calculation_rent(house_id: int, month: int):
    """
    Расчет коммунальных платежей.
    id_house - id дома в DB
    month - порядковый номер месяца от 1 до 12
    """
    prev_month_readings = WaterMeter.objects.filter(
            date__month=(month - 1),
            date__year=date.today().year,
            apartment=OuterRef('pk'),
            tariff=OuterRef('water_meter__tariff')
        )

    qw_st = (
            Apartment.objects.filter(house=house_id)
            .prefetch_related('water_meter')
            .filter(
                water_meter__date__month=month,
                water_meter__date__year=date.today().year
            ).alias(
                previous_value=Subquery(prev_month_readings.values('value')),
                cost=((F('water_meter__value') - F('previous_value'))
                      * F('water_meter__tariff'))
            ).values('number').annotate(cost_water=Sum('cost'),
                                        cost_property=F('area')
                                        * F('house__tariff_property__price'))
        )
    add_bill_in_db(qw_st, house_id)
