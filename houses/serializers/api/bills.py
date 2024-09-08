from rest_framework import serializers

from houses.models.bills import Billing


class BillingSerializer(serializers.ModelSerializer):
    """Сериализатор квартплаты."""

    class Meta:
        model = Billing
        fields = '__all__'
