# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

def runner():
    def vars_input_1():
        def iterator_int_since_param(res, fin_el):
            for el in count(res):
                if el > fin_el:
                    break
                else:
                    print(el)
                    # почему-то при вызове функции через return print(iterator_int_since_param(res, fin_el),
                    # где в самой функции после "else:" не print, а return (Вы говорили, так правильнее)
                    # помимо нужного списка добавляется в конце значение "None"

        # блок выбора данных: демо или введённые пользователем
        def test_data():
            # функция подставляет тестовые данные в случае их отсутствия или некорректного ввода
            print(f'Использую в качестве параметра тестовые данные:')
            test_res = 3
            test_fin_el = 10
            print(f'Начало: {test_res}')
            print(f'Конец: {test_fin_el}')
            res = test_res
            fin_el = test_fin_el
            return iterator_int_since_param(res, fin_el)
        res_str = input("Введите стартовое целое число: ")
        fin_el = input("Введите конечное целое число: ")
        if res_str != '' and fin_el != '':
            try:
                res = int(res_str)
                fin_el = int(fin_el)
            except ValueError:
                print(f'Введённые данные не соответствуют условию.')
                return test_data()
        else:
            print(f'Данные не предоставлены.')
            return test_data()
        # конец блока выбора данных
        return iterator_int_since_param(res, fin_el)




    def vars_input_2():


        def repeat_el_lst(res_l, stop_param):
            c = 0
            for el in cycle(res_l):
                if c > stop_param-1:
                    break
                print(el)
                c += 1

        print('Сейчас будем повторять несколько раз один и тот же список чисел.')

        # блок выбора данных: демо или введённые пользователем
        res_l = []
        def test_data():
            # функция подставляет тестовые данные в случае их отсутствия или некорректного ввода
            print(f'Использую в качестве параметра тестовые данные:')
            test_cycle_lst = [1, 2, 3]
            test_stop_param = 3
            print(f'Тестовый список: {test_cycle_lst}')
            print(f'Количество итераций: {test_stop_param}')
            res_l = test_cycle_lst
            stop_param = test_stop_param*len(res_l)
            return repeat_el_lst(res_l, stop_param)

        cycle_lst = input("Введите список из целых чисел через пробел: ").split()
        stop_param = input("Введите, сколько раз повторить список: ")
        if cycle_lst != '' and stop_param != '':
            try:
                # допущение, что итерируется список из целых чисел, иначе можно указать float
                for el in cycle_lst:
                    cycle_lst = int(el)
                    res_l.append(el)
                stop_param = int(stop_param)*len(res_l)
            except ValueError:
                print(f'Введённые данные не соответствуют условию.')
                return test_data()
        else:
            print(f'Данные не предоставлены.')
            return test_data()

        repeat_el_lst(res_l, stop_param)



    vars_input_1()
    vars_input_2()


runner()