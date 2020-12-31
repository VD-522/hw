# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def task4_5():

    def even_multiply(prev_el, el):
         return prev_el * el

    print(reduce(even_multiply, [num for num in range(100, 1000 + 1) if num % 2 == 0]))


task4_5()
