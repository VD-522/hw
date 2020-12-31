# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv as argv
from sys import exit as exit


def salary(hours, hour_rate, bonus):
    wage = hours * hour_rate
    salary = hours * hour_rate + bonus
    print(f'З.п. сотрудника составляет: {salary} у.е., в т.ч. осн. часть: {wage} у.е. и бонус: {bonus} у.е.')


def help_if_terminal_error():
    print(f'Ошибка. Вызовите модуль через терминал. \n'
          f'Синтаксис: "task4_1.py hours hour_rate bonus". \n'
          f'Тип данных: десятичные. Всего параметров: 3'
          f'Далее пример работы функции для данных: "1, 2, 3.5":')
    salary(1, 2, 3.5)


# хотел сделать 2 способа ввода параметров - через input, если скрипт запущен в PyCharm, а не через Терминал .
# ...но не понял, как :)
"""
def input4_1():
    try:
        hours, hour_rate, bonus = input(
            "Введите через пробел выработку в часах, ставку в час, премию сотрудника\n").split()
            
# почему не работает присвоение float списку элементов в input? Т.е.:
# hours, hour_rate, bonus = float(input(...)
# --> TypeError: float() argument must be a string or a number, not 'list'
# есть ли способ в одну строку присвоить группе элементов списка input нужный тип данных?

        hours = float(hours)
        hour_rate = float(hour_rate)
        bonus = float(bonus)
        salary(hours, hour_rate, bonus)
    except ValueError:
        print("Ошибка. Повторите ввод параметров. Тип данных: десятичные. Всего параметров: 3")
"""


def process_argv():
    if len(argv) != 4:
        help_if_terminal_error()
        exit()
    else:
        try:
            for el in argv:
                el = float(el)

        except ValueError:
            help_if_terminal_error()

        salary(float(argv[1]), float(argv[2]), float(argv[3]))
        # почему при вызове salary приходится снова явно указывать тип float,
        # хотя в try для каждого el уже задан тип el = float(el)


# при выборе, запрашивать ли параметры у пользователя или считывать их, я думал, подойдёт if main:
if __name__ == "__main__":
    # по моей идее, тут логика, если через терминал и с заданными заранее параметрами в командной строке:
    print(f'I am running as an independent program with name = %s' % __name__)
    process_argv()
else:
    # а тут логика, если через PyCharm
    print('I am running as an imported module with name = %s' % __name__)
    # input4_1()
    # но пришлось закомментить, т.к. подобный подход не сработал :(

# не посоветуете ли, как сделать подобную логику (ввод данных, если через PyCharm, использовать параметры,
# если модуль запущен в Терминале с указанными параметрами, справка, если параметры не указаны)?
# Спасибо :)