from django.db import models


class Billing(models.Model):
    """Модель квартплаты."""
    apartment = models.ForeignKey(
        'houses.Apartment', models.CASCADE, verbose_name='Квартира',
    )
    cost_water = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Водоснабжение',
    )
    cost_property = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Имущество',
    )
    date = models.DateField(auto_now_add=True, verbose_name='Дата показаний')

    class Meta:
        ordering = ('apartment',)
        verbose_name = 'Квартплата'
        verbose_name_plural = 'Квартплаты'

    def __str__(self):
        return str(self.apartment)
