from django.urls import path

from .views import *


urlpatterns = [
    path('', cars_views, name='cars'),
]
