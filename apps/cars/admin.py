from django.contrib import admin

from .models import Car, Brand, CarInventory


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'model',
        'brand',
        'factory_year',
        'model_year',
        'value'
    )
    search_fields = (
        'model',
        'brand',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)

admin.site.register(Car, CarAdmin)

admin.site.register(CarInventory)
