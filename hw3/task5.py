# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

from sys import exit

sum_list = []

def task5(new_list):
    for el in new_list:
        el = float(el)
        sum_list.append(el)
    print(f'Суммируем список из элементов: {sum_list}')
    task_sum = sum(sum_list)
    return task_sum


def vars_input():
    try:
        new_list = input("Введите суммируемые числа через пробел и нажмите Enter (введите q в конце, чтобы суммировать и выйти):\n").split()
        if 'q' in new_list:
            new_list.remove('q')
            for element in new_list:
                element = float(element)
            return print(task5(new_list)), exit()
        else:
            for element in new_list:
                element = float(element)
            return print(task5(new_list)), vars_input()
    except ValueError:
        print('Введённые данные не соответствуют указанным условиям, пожалуйста, повторите.')
        return vars_input()


vars_input()
