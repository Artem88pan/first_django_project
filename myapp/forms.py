from django import forms
import datetime


def year_choices():
    return [(r, r) for r in range(1970, datetime.date.today().year+1)]

def corrent_year():
    return datetime.date.today().year

class CarForm(forms.Form):
    brand = forms.CharField(max_length=30, label='бренд')
    model = forms.CharField(max_length=30, label='модель')
    color = forms.CharField(max_length=30, label='цвет', required=False)
    power = forms.IntegerField(label='мощность', required=False, min_value=1, max_value=600)
    year = forms.ChoiceField(label='год производства',choices=year_choices, initial=corrent_year)

