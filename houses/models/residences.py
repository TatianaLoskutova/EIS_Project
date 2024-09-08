from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class House(models.Model):
    """Модель дома."""
    address = models.CharField(max_length=100, unique=True, verbose_name='Адрес дома')
    tariff_property = models.ForeignKey(
        'houses.Tariff', on_delete=models.CASCADE,
        verbose_name='Тариф имущества',
    )

    class Meta:
        ordering = ('address',)
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return self.address


class Apartment(models.Model):
    """Модель квартиры."""
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер квартиры',
        validators=[MinValueValidator(1), MaxValueValidator(5000)],
    )
    area = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name='Площадь квартиры',
    )
    house = models.ForeignKey('houses.House', models.CASCADE)

    class Meta:
        ordering = ('number',)
        default_related_name = 'apartments'
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

        constraints = [
            models.UniqueConstraint(
                fields=['number', 'house'],
                name='unique_measurement_unit'
            )
        ]

    def __str__(self):
        return str(self.number)
