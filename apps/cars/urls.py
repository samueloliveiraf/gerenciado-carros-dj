from django.urls import path

from .views import *


urlpatterns = [
    path('', cars_views, name='cars'),
    path('cars/new/', car_create_view, name='car_create_view')
]
