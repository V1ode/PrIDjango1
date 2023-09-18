from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Страница приложения для Людей')
def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')