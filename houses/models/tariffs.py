from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class WaterMeter(models.Model):
    """Модель счетчика воды."""
    value = models.PositiveIntegerField(
        verbose_name='Показания счетчика',
        validators=[MinValueValidator(1), MaxValueValidator(99999)],
        help_text='Введите показания до запятой'
    )
    date = models.DateField(default=timezone.now, verbose_name='Дата показаний')
    apartment = models.ForeignKey(
        'houses.Apartment', models.CASCADE, verbose_name='Квартира',
    )

    class Meta:
        ordering = ('apartment',)
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
        # default_related_name = 'tariffs'
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name
