from django.urls import path
from .views import about, login, contacts, index_myapp, cars, drivers, add_car

urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('contacts/<int:id>/', contacts, name='contacts'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('add_car', add_car, name='add_car'),
]