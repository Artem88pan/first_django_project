import django_filters
from .models import Car

class CarFilters(django_filters.FilterSet):
    model = django_filters.CharFilter(field_name='model', lookup_expr='icontains', label='модель')



    class Meta:
        model = Car
        fields = ['brand', 'model', 'year']