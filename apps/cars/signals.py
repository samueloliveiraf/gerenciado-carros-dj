from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from apps.cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_values = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_values=cars_values
    )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
