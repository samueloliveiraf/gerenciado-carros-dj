from django.db import models

from core.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(
        max_length=200
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Car(BaseModel):
    model = models.CharField(
        max_length=200
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='car_brand'
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
    plate = models.CharField(
        max_length=10,
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='card/',
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'Modelo = {self.model} | Marca = {self.brand}'

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
