from rest_framework import serializers

from houses.models.residences import Apartment, House


class ApartmentSerializer(serializers.ModelSerializer):
    """Сериализатор квартиры."""

    class Meta:
        model = Apartment
        fields = ('id', 'number', 'area', 'house',)
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


class HouseSerializer(serializers.ModelSerializer):
    """Сериализатор дома."""

    class Meta:
        model = House
        # fields = ('apartments', 'address')
        fields = ('id', 'address',)
