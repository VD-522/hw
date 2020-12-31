# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

def get_el_if_next_is_more(res):
    print('На основе указанного списка данных привожу список элементов, которые больше предыдущих:')
    next_is_more_list = []
    for i in range(1, len(res)):
        if res[i] > res[i -1]:
            next_is_more_list.append(res[i])
    return next_is_more_list


def input4_2():
    res_l = []
    try:
        res_str = input("Введите список чисел через пробел: ").split()
        for el in res_str:
            el = int(el)
            res_l.append(el)
        if res_l == '':
            print("Недостаточно данных. Повторите. Тип данных: целые. А пока использую тестовую последовательность.")
            test_res_l = [7, 9, 3, 5, 1, 10]
            print(f'Список {test_res_l}')
            res_l = test_res_l
            print(get_el_if_next_is_more(res_l))
        else:
            print(get_el_if_next_is_more(res_l))
    except ValueError:
        print("Ошибка типа данных. Повторите. Тип данных: целые. А пока использую тестовую последовательность.")
        test_res_l = [7, 9, 3, 5, 1, 10]
        print(f'Список {test_res_l}')
        res_l = test_res_l
        print(get_el_if_next_is_more(res_l))


input4_2()