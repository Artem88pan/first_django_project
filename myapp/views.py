from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

menu = [{'title':"О сайте", 'url_name': 'about'},
        {'title': "машины парка", 'url_name': 'cars'},
        {'title': " Водители парка",'url_name':'drivers'},
        ]



def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)

def cars(request):
    title = 'Машины'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)

def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/drivers.html', context=context)



def login(request):
    return HttpResponse('page login')

def contacts(request,id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name':name, 'age': age}
    return HttpResponse(f'page contacts, url_paramttr_id = {url_id}, get_params - {get_params}')


def index_myapp(request):
    title = 'моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)

def index(request):
    return HttpResponse('main page')

