from django.contrib import admin
from .models import Driver, Car, Employee, Client, CarBrand
# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(CarBrand)
