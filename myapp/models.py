from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    is_activated = models.BooleanField(verbose_name='активация')


    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='бренд')
    model = models.CharField(max_length=30, verbose_name='модель')
    color = models.CharField(max_length=30, verbose_name='цвет')
    power = models.IntegerField(verbose_name='мощность')
    year = models.IntegerField(verbose_name='год производства')

    def __str__(self):
        return self.brand


    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Машины'
