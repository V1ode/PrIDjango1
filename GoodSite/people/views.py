from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render, redirect
import re

class data_handler:
    def __init__(self, year):
        #raise PermissionDenied()
        self.year = year
        self.dates = {
            2015: 'Было хорошо',
            2016: 'Я уже не помню',
            2017: 'Я уже не помню',
            2018: 'Было неплохо',
            2019: 'Было хорошо',
            2020: 'Было чудесно',
            2021: 'Домашний арест',
            2022: 'Танцы с красоткой',
            2023: 'Есть',
            2024: 'Возможно, будет хорошо',
            2025: 'Будет хорошо'
        }


    def return_date_info(self):
        return self.dates[self.year]


pri_info = {
        '1' : ['Абрамов Александр Альбертович', '22-2.034'],
        '2' : ['Близнюк Илья Сергеевич', '22-2.035'],
        '3' : ['Зверев Андрей Александрович', '22-2.036'],
        '4' : ['Карагузин Максим Игоревич', '22-2.037'],
        '5' : ['Круглик Евгений Дмитриевич', '22-2.038'],
        '6' : ['Лысков Влас Евгеньевич', '22-2.039'],
        '7' : ['Маклюсов Роман Романович', '21-2.010'],
        '8' : ['Манешин Антон Сергеевич', '22-2.040'],
        '9' : ['Петрачков Александр Викторович', '22-2.041'],
        '10' : ['Сафонов Глеб Александрович', '22-2.045'],
        '11' : ['Терешин Роман Павлович 🎶(❁´◡`❁)', '22-2.042'],
        '12' : ['Чертков Федор Андреевич', '22-2.043'],
    }

# Create your views here.
def index(request):
    out = dict(request.GET)
    out = out.values()
    return HttpResponse(f"Страница для Людей")


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_group(request):
    out = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_info.items():
        out += number + '.'
        out += mas_of_info[0]
        out += '</p>'
    return HttpResponse(out)


def pri_id(request, number_student):
    # if number_student > 30:
    #     return redirect('/', permanent=True)
    if str(number_student) in pri_info:
        out = '<h1> ПрИ-201 </h1> <p>'
        mas_of_info = pri_info[str(number_student)]
        for info in mas_of_info:
            out += info + ' '
        out += '</p>'
        return HttpResponse(out)
    else:
        out = '<h1> Ошибка </h1> <h3> Такого студента не существует </h3>'
        return HttpResponse(out)


def post_detail(request):
    if request.GET:
        info = dict(request.GET)
        out = ""
        for i, j in info.items():
            out += i
            out += "="
            out += j[0]
            out += " | "
        out = out[:-2]
        return HttpResponse(f'<h1>{out}</h1>')
    else:
        return HttpResponse(f'<h1>Get is empty</h1>')


def redirect_to_home(request):
    return redirect(index)


def redirect_to_Eugen(request, name):
    if re.fullmatch(r'[Ee]ugen', name):
        return redirect('spisok_pri', '5')


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def server_down(exception):
    return HttpResponseServerError('<h1> Сервер себя плохо чувствует. Страница недоступна <h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес!!! </h1>')


def forbidden(request, exception):
    return HttpResponseForbidden('<h1> Доступ ЗАПРЕЩЕН <h1>')


def bad_request(request, exception):
    return HttpResponseBadRequest('<h1> Мы не поняли ваш запрос <h1>')


def date_handler(request, year):
    out = data_handler(year)
    return HttpResponse(out.return_date_info())