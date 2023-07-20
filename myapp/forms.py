from django import forms
from django.conf.global_settings import DATE_INPUT_FORMATS
from django.forms import ModelForm
from .models import *
import datetime
from project_django.settings import DATE_INPUT_FORMAT


def year_choices():
    return [(r, r) for r in range(1970, datetime.date.today().year+1)]

def corrent_year():
    return datetime.date.today().year

#class CarForm(forms.Form):
   # brand = forms.CharField(max_length=30, label='бренд')
   # model = forms.CharField(max_length=30, label='модель')
   # color = forms.CharField(max_length=30, label='цвет', required=False)
   # power = forms.IntegerField(label='мощность', required=False, min_value=1, max_value=600)
  #  year = forms.ChoiceField(label='год производства',choices=year_choices, initial=corrent_year)
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['age']

    birthday = forms.DateField(input_formats=DATE_INPUT_FORMAT, label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = '__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['is_activated']


class EmployeeForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee
        fields = '__all__'

