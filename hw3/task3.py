# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(var_1, var_2, var_3):
    params = set([var_1, var_2, var_3])
    if len(params) == 3:
        params.remove(min(params))
        return f'Сумма двух наибольших аргументов равна: {sum(params)}'
    elif len(params) == 2:
        return f'Сумма двух наибольших аргументов равна: {sum(params)}'
    else:
        return f'Сумма двух наибольших аргументов равна: {sum(params)*2}'


def vars_input():
    try:
        a, b, c = input("Введите через пробел три числа: ").split()
        a = float(a)
        b = float(b)
        c = float(c)
        print(my_func(a, b, c))
    except ValueError:
        print('Не могу распознать три числа, пожалуйста, повторите.')
        return vars_input()

vars_input()
