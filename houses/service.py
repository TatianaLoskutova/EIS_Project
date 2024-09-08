from django.db.models.query import QuerySet

from houses.models.bills import Billing
from houses.models.residences import Apartment


def add_bill_in_db(qw_st: QuerySet[Billing], house_id: int) -> None:
    """Добавление Bill в БД."""
    data = []

    for value in qw_st:
        number = value.get('number')
        cost_water = value.get('cost_water')
        cost_property = value.get('cost_property')
        data.append(
            Billing(
                apartment=Apartment.objects.filter(number=number,
                                                   house=house_id)[0],
                cost_water=cost_water,
                cost_property=cost_property
            )
        )

    Billing.objects.bulk_create(
        data,
        ignore_conflicts=True
    )
