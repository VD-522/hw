# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

def runner4_4():
    def unique_el_list(res_l):
        print(f'Определяю элементы списка, не имеющие повторений.')
        lst_of_unique_el = []
        for i in res_l:
            if res_l.count(i) == 1:
                lst_of_unique_el.append(i)
        if lst_of_unique_el == []:
            return f'В данном списке все элементы повторяются.'
        else:
            return lst_of_unique_el


    def vars_input():
        def test_data():
            # функция подставляет тестовые данные в случае их отсутствия или некорректного ввода
            print(f'Использую в качестве параметра тестовые данные:')
            test_res_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
            print(f'{test_res_l}')
            res_l = test_res_l
            return print(unique_el_list(res_l))


        res_str = input("Введите список целых чисел через пробел: ").split()
        res_l = []

        if res_str != '':
            try:
                for el in res_str:
                    # здесь - допущение по условию, что тип данных - целые числа. Иначе - float.
                    el = int(el)
                    res_l.append(el)
            except ValueError:
                print(f'Введённые данные не соответствуют условию.')
                return test_data()
        else:
            print(f'Данные не предоставлены.')
            return test_data()

        print(unique_el_list(res_l))


    vars_input()


runner4_4()