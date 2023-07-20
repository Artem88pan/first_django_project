from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from.forms import CarForm, ClientForm, DriverForm, EmployeeForm
from .models import *
import datetime
from .filters import CarFilters
# Create your views here.

menu = [{'title':"О сайте", 'url_name': 'myapp:about'},
        {'title': "машины парка", 'url_name': 'myapp:cars'},
        {'title': " Водители парка",'url_name':'myapp:drivers'},
        {'title': " клиенты",'url_name':'myapp:clients'},
        {'title': "сотрудники", 'url_name':'myapp:employee_list'},
        {'title': "Заказы", 'url_name':'myapp:order_list'},
        ]



def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)

@login_required
def cars(request):
    title = 'Машины'
    f = CarFilters(request.GET, queryset=Car.objects.all())
    if not request.GET.get('query'):
        cars = Car.objects.all()

    context = {'title': title, 'menu': menu, 'cars': cars, 'filter': f}
    return render(request, 'myapp/cars.html', context=context)

def drivers(request):
    title = 'Водители'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'objects': drivers}
    return render(request, 'myapp/drivers.html', context=context)


def add_drivers(request):
    if request.method == 'GET':
        title = 'Добавить Водителя'
        form = DriverForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/add_drivers.html', context=context)

    if request.method == 'POST':
        driverform = DriverForm(request.POST)
        if driverform.is_valid():
            driverform.save()
            return drivers(request)


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
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)



def add_client(request, title=None):
    
    title = 'добавить клиента'
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instanse = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instanse.age = age
            instanse.save()
            #form.save()
            return clients(request)
    else:
            form = ClientForm
            
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/client_add.html', context=context)
@staff_member_required
def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)

def client_card(request, pk):
    title = 'Client info'
    client = Client.objects.get(pk=pk)
    context = {'menu': menu, 'title': title, 'client': client}
    return render(request, 'myapp/client_card.html', context=context)




def cars(request):
    title = 'Машины'
    f = CarFilters(request.GET, queryset=Car.objects.all())
   # if not request.GET.get('query'):
        #cars = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': cars, 'filter': f}
    return render(request, 'myapp/cars.html', context=context)

def car_card(request, pk):
    title = 'Car info'
    car = Car.objects.get(pk=pk)
    context = {'title': title, 'menu': menu, 'car': car}
    return render(request, 'myapp/car_card.html', context=context)

class EmployeeList(ListView):
    model = Employee
    template_name = 'myapp/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 4

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сотрудники'
        context["count"] = Employee.objects.count()
        return  context

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'myapp/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu
        return context

class EmployeeCreate(CreateView):
    model = Employee
    #fields = '__all__'
    form_class = EmployeeForm
    template_name = 'myapp/employee_form.html'


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'myapp/employee_update.html'


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('employee_list')


class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'myapp/order_form.html'


class OrderList(ListView):
    model = Order
    template_name = 'myapp/order_list.html'
    context_object_name = 'objects'

def car_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        ft = Q(model__icontains=query) | Q(brand__name__icontains=query)
        results = Car.objects.filter(ft)

        return cars(request, cars = results)

