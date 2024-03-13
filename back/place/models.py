from django.db import models
from django.utils import timezone


class Place(models.Model):
    address_place = models.CharField(
        verbose_name='Адрес',
        max_length=50,
        db_index=True
    )
    lat = models.DecimalField(
        verbose_name='Широта',
        max_digits=10,
        decimal_places=2
        )
    lon = models.DecimalField(
        verbose_name='Долгота',
        max_digits=10,
        decimal_places=2
        )
    request_date = models.DateField(
        verbose_name='Дата запроса',
        default=timezone.now
    )

    class Meta:
        unique_together = ['address_place', 'lat', 'lon']
