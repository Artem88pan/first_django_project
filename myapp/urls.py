from django.urls import path
from .views import about, login, contacts, index_myapp, cars, drivers, add_car, add_client, clients, client_card, \
    car_card

urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('contacts/<int:id>/', contacts, name='contacts'),
    path('cars/<int:pk>/', car_card, name='car_card'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('add_car', add_car, name='add_car'),
    path('clients/<int:pk>/', client_card, name='client_card'),
    path('add_client/', add_client, name='add_client'),
    path('clients/', clients, name='clients'),
]