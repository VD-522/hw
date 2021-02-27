# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __add__(self, other):
        other = other.complex
        complex_op = self.complex + other
        return ComplexNum(complex_op.real, int(complex_op.imag))

    def __mul__(self, other):
        other = other.complex
        complex_op = self.complex * other
        return ComplexNum(complex_op.real, int(complex_op.imag))

    def __str__(self):
        return self.complex.__str__()


if __name__ == '__main__':
    c1 = ComplexNum(2, -3)
    c2 = ComplexNum(3, -4)

    print(c1 + c2, complex(2, -3) - complex(5))
    print(c1 * c2, complex(3, -4) / complex(10))
