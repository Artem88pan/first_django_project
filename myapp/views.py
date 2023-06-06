from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse('About site')

def login(request):
    return HttpResponse('page login')

def contacts(request,id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name':name, 'age': age}
    return HttpResponse(f'page contacts, url_paramttr_id = {url_id}, get_params - {get_params}')


def index_myapp(request):
    return HttpResponse('myapp page')

def index(request):
    return HttpResponse('main page')

