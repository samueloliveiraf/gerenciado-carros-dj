from django.urls import path

from .views import *


urlpatterns = [
    path('', CarsListView.as_view(), name='cars'),
    path('cars/new/', NewCarCreateView.as_view(), name='car_create_view'),
    path('cars/<str:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<str:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<str:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]
