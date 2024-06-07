from django.db import models
from core.models import BaseModel


class Car(BaseModel):
    model = models.CharField(
        max_length=200
    )
    brand = models.CharField(
        max_length=200
    )
    factory_year = models.IntegerField(
        blank=True, null=True
    )
    model_year = models.IntegerField(
        blank=True, null=True
    )
    value = models.FloatField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
