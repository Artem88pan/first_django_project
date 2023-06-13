from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from.forms import CarForm
# Create your views here.

menu = [{'title':"О сайте", 'url_name': 'about'},
        {'title': "машины парка", 'url_name': 'cars'},
        {'title': " Водители парка",'url_name':'drivers'},
        {'title': " клиенты",'url_name':'drivers'},
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
    title = 'моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)

@csrf_protect
def login(request):
    title = 'войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username}, Password - {password}')

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)


def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)
    if request.method == 'POST':
        carform = CarForm(request,POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
