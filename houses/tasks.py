from datetime import date

from celery import shared_task

from .models.bills import Billing
from .models.residences import Apartment


@shared_task(name='calculation_bills')
def calculation_rent(house_id: int, month: int):
    """
    Расчет коммунальных платежей.
    id_house - id дома в DB
    month - порядковый номер месяца от 1 до 12
    """
    apartments = (
        Apartment.objects.filter(house=house_id)
        .prefetch_related('water_meter')
        .filter(
            water_meter__date__month=month,
            water_meter__date__year=date.today().year
        )
    )

    for apartment in apartments:
        current_water_month_reading = apartment.water_meter.latest('date').value
        prev_water_month_reading = apartment.water_meter.filter(
            date__month=(month - 1), date__year=date.today().year,
        ).latest('date').value
        consumption = current_water_month_reading - prev_water_month_reading

        cost_water = consumption * apartment.tariff.price
        cost_property = apartment.area * apartment.tariff.price

        Billing.objects.bulk_create([
            Billing(
                apartment=apartment,
                cost_water=cost_water,
                cost_property=cost_property,
            )
        ], ignore_conflicts=True)
