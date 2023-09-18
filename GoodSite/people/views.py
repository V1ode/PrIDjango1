from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Страница приложения для Людей')


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_id(request, number_student):
    return HttpResponse(f'<h1> ПрИ-201 </h1> <p>Студент под номером {number_student}</p>')


def categories(request, cat):
    return HttpResponse(f'<h1> Ссылка {cat} </h1>')