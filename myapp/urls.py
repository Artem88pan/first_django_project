from django.urls import path
from .views import about, login, contacts, index_myapp, cars, drivers, add_car, add_client, clients, client_card, \
    car_card, EmployeeList, EmployeeDetail, EmployeeCreate, EmployeeUpdate, EmployeeDelete, OrderList, OrderCreate, add_drivers, car_search

app_name = 'myapp'

urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('contacts/<int:id>/', contacts, name='contacts'),
    path('cars/<int:pk>/', car_card, name='car_card'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('add_drivers/', add_drivers, name='add_drivers'),
    path('add_car', add_car, name='add_car'),
    path('clients/<int:pk>/', client_card, name='client_card'),
    path('add_client/', add_client, name='add_client'),
    path('clients/', clients, name='clients'),
    path('employees/',EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees_form/', EmployeeCreate.as_view(),name='employee_form'),
    path('employees/<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('order_form/', OrderCreate.as_view(), name='order_form'),
    path('cars/search/', car_search, name='car_search'),
]