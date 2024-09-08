from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class WaterMeter(models.Model):
    """Модель счетчика воды."""
    value = models.PositiveIntegerField(
        verbose_name='Показания счетчика',
        validators=[MinValueValidator(1), MaxValueValidator(99999)],
        help_text='Введите показания до запятой'
    )
    date = models.DateField(default=date.today(), verbose_name='Дата показаний')
    tariff = models.ForeignKey('houses.Tariff', models.CASCADE, verbose_name='Тариф')
    apartment = models.ForeignKey(
        'houses.Apartment', models.CASCADE, 'watermeter', verbose_name='Квартира',
    )

    class Meta:
        ordering = ('tariff',)
        default_related_name = 'water_meter'
        verbose_name = 'Счетчик воды'
        verbose_name_plural = 'Счетчики воды'

    def __str__(self):
        return str(self.value)


class Tariff(models.Model):
    """Модель тарифа."""
    NAME_TARIFF = [
        ('water', 'Вода'),
        ('property', 'Имущество')
    ]
    name = models.CharField('Название', choices=NAME_TARIFF, unique=True, max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name
