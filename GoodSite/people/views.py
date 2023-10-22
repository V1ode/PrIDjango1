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


class DataBase:
    __instance = None
    __connect = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None
        self.__connect = None

    def __init__(self, user, psw, port):
        if self.__connect is None:
            self.user = user
            self.psw = psw
            self.port = port
            self.data = "DATA"

    def connect(self):
        print(f"Соединение с Базой данных:{self.user}, "
              f"{self.psw}, {self.port}")

    def close(self):
        print("Закрыть соединение с Базой данных")

    def read(self):
        return "Данные из Базы данных"

    def write(self):
        print(f"Запись в Базу данных {self.data}")


def split_line(line, sep):
    parse_line = line
    list = []
    i = 0
    last_i = 0
    no_sep = True

    if line == len(line)*' ':
        list.append('')
    else:
        while(i < len(line)):
            if parse_line[i] == "\"":
                list.append(parse_line[i+1:parse_line.find("\"")])
                if parse_line.find("\"") == len(line)-1:
                    break
                else:
                    i = parse_line.find("\"") + 1
            if parse_line[i] == sep:
                if i == len(line)-1:
                    list.append(parse_line[:i])
                    list.append("\"")
                    break
                elif parse_line[i+1] == sep:
                    list.append(parse_line[:i])
                    list.append("\"")
                    i = i+1
                else:
                    list.append(parse_line[:i])
                    i = i + 1
                no_sep = False
        i += 1
    if no_sep:
        list.append(line)
    return list


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


dict_w_object_types = {
    'int' : '1',
    'float' : 1.1,
    'str' : 'some_string',
    'list' : [1, 2, 3],
    'dict' : {'key' : 'value'},
    'tuple' : [4, 5, 6],
    'set' : {'seven', 'eight'},
    'bool' : True,
}

# Create your views here.
def index(request):
    return render(request, 'people/index.html')

def object_types(request):
     return render(request, 'people/object_types.html', context=dict_w_object_types)


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def test_split_line(request, line, sep):
    list = split_line(line, sep=sep)

    empty = ''
    first_out = ''
    second_out = ''

    if list[0] == '':
        empty = "Строка пуста"
    else:
        first_out = f'Результаты работы функции split_line по строке {line} с разделителем "{sep}" :'
        for item in list:
            second_out += item
            second_out += '\t'

    result = {}
    result['empty'] = empty
    result['first_str'] = first_out
    result['second_str'] = second_out
    result['list'] = list[0]
    return render(request, 'people/Split_line Tester.html', context=result)


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