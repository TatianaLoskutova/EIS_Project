from rest_framework import serializers
from datetime import date

from houses.models.tariffs import WaterMeter


class WaterMeterSerializer(serializers.ModelSerializer):
    """Сериализатор счетчика."""

    class Meta:
        model = WaterMeter
        fields = '__all__'

    def validate_value(self, value):
        if value <= 0 or value > 99999:
            raise serializers.ValidationError('Значение должно быть от 1 до 99999')
        return value

    def create(self, validated_data):
        """
        Повторное отправление данных в текущем месяце обновит данные в БД.
        """

        value = validated_data.pop('value')

        if WaterMeter.objects.filter(
            date__month=date.today().month,
            date__year=date.today().year,
            **validated_data
        ).exists():

            water_meter = WaterMeter.objects.filter(
                **validated_data
            )[0]
            water_meter.value = value
            water_meter.save()
        else:
            water_meter = WaterMeter.objects.create(
                value=value,
                **validated_data)
        return water_meter
