# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения 2х объектов класса Matrix (2х матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""К сожалению эта задача решена в корне неверно. В конструкторе должен быть 1 список, а не 2.
И складывать надо разные объекты

 @VD-522	Reply…
hw7/task7_1.py

 print(sum_matrix.__add__())

 # не придумал, как реализовать логику сложения матриц различной размерности, т.е. чтобы

 @legacy72 legacy72 9 days ago
Нужно передавать размер и инициализировать список в цикле. Но это не главная проблема этой задачи)"""


""" ну тогда так :) """
# без логики сложения матриц разной размерности:


# class Matrix:
#     def __init__(self, mtx):
#         self.mtx = mtx
#
#     def __add__(self, other):
#         mtx = self.mtx
#         other = other.mtx
#
#         for i in range(len(self.mtx)):
#             for j in range(len(other[i])):
#                 mtx[i][j] = self.mtx[i][j] + other[i][j]
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mtx]))
#
#
# # реализовано только для матриц одинаковой размерности 4 на 3:
# mtx1 = Matrix([[3, 5, 32, 0],
#           [2, 4, 6, 0],
#           [3, 33, 3, 3]])
#
# mtx2 = Matrix([[8, 6, 9, 1],
#          [0, 8, 6, 2],
#          [0, 0, 0, 0]])
#
# sum_matrix = mtx1.__add__(mtx2)
# print(sum_matrix)


""" ********************************************************************************************** """
# с логикой сложения матриц разной размерности:


class InvalidException(Exception):
    def __init__(self, param):
        print(f'>> Сработало исключение:')
        print(f'>> Недопустимое значение')
        self.txt = param
        exit()


class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx
        self.len_mtx = len(mtx)

        def check_mtx_equal_args():
            for i in range(0, len(mtx)):
                if len(mtx[i-1]) != len(mtx[i]):
                    print(f'Ошибка. Длина списков в одной из матриц не одинаковая.')
                    exit()

        check_mtx_equal_args()

    def __add__(self, other):
        mtx = self.mtx
        other = other.mtx

        try:
            def check_mtx_arg_len():
                for k in range(0, len(mtx)):
                    if len(mtx[k]) != len(other[k]):
                        if len(mtx[k]) < len(other[k]):
                            while len(mtx[k]) < len(other[k]):
                                mtx[k].append(0)
                        elif len(mtx[k]) > len(other[k]):
                            while len(mtx[k]) > len(other[k]):
                                other[k].append(0)

            def check_mtx_len():
                if self.len_mtx != len(other):
                    add_arg = []
                    if self.len_mtx > len(other):
                        while len(add_arg) < len(other[0] or len(add_arg) < len(mtx[0])):
                            add_arg.append(0)
                        while self.len_mtx != len(other):
                            other.append(add_arg)

                    elif self.len_mtx < len(other):
                        while len(add_arg) < len(other[0]) or len(add_arg) < len(mtx[0]):
                            add_arg.append(0)
                        mtx.append(add_arg)

            check_mtx_len()
            check_mtx_arg_len()

            for i in range(len(self.mtx)):
                for j in range(len(other[i])):
                    mtx[i][j] = self.mtx[i][j] + other[i][j]
            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mtx]))

        except InvalidException(Exception):
            print(f'Ошибка ввода. Скрипт завершён')
            exit()


if __name__ == '__main__':
    print(f'Суммируем первую пару матриц:')
    mtx2 = Matrix([[8, 6, 9],
                   [17, 18, 19],
                   [10, 10, 10]])

    mtx1 = Matrix([[3, 6, 4, 14],
                   [4, 4, 14, 24]])

    sum_matrix = mtx1.__add__(mtx2)
    print(sum_matrix)

    print(f'\nСуммируем вторую пару матриц:')
    mtx3 = Matrix([[8, 6, 9],
                   [17, 18],
                   [10, 10, 10]])

    mtx4 = Matrix([[3, 6, 4, 14],
                   [4, 4, 14, 24]])

    sum_matrix = mtx3.__add__(mtx4)
    print(sum_matrix)


""" извиняюсь, если много избыточного кода ^_^ """