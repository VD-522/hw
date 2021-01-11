# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия 1 кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asp_mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, depth):
        super().__init__(_length, _width)
        self.depth = depth

try:
    r = MassCount(float(input('Введите длину дороги в м (натур. число0), например 5000: ')),
                  float(input('Введите ширину дороги в м (натур. число), например 25: ')),
                  float(input('Введите толщину дороги в см (натур число), например 5: ')))
except ValueError:
    print('Введённые данные неверны, попробуйте заново.')
    print('Ниже - рассчёт для параметров 5000, 25, 5:')
    r = MassCount(5000, 25, 5)

print((f'Масса асфальта, необходимая для дороги с указанными параметрами, равна {r.asp_mass()} кг.'))