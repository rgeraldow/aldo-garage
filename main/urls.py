from django.urls import path
from main.views import show_main, create_car_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-car-entry', create_car_entry, name='create_car_entry'),
]