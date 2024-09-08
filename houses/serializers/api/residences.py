from rest_framework import serializers

from houses.models.residences import Apartment, House
from houses.serializers.api.tariffs import WaterMeterSerializer


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор дома."""
    apartments = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ('apartments', 'address', 'tariff_property')

    def get_apartments(self, obj):
        """Получение квартир."""
        return obj.apartments.values('id', 'number', 'area', 'house')


class ApartmentSerializer(serializers.ModelSerializer):
    """Сериализатор квартиры."""
    water_meter = WaterMeterSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('water_meter', 'number', 'area', 'house')
        read_only_fields = ('water_meter',)
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Apartment.objects.all(),
                fields=['number', 'house'],
                message='Квартира с таким номером уже создана ранее.'
            )
        ]

        def validate_number(self, value):
            if value <= 0 or value > 5000:
                raise serializers.ValidationError(
                    'Веден неверный номер квартиры. Значение должно быть от 1 до 5000'
                )
            return value
