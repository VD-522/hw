# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), кот. должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость гражданского авто {self.name} - {self.speed} км/ч')

        if self.speed > 60:
            return f'{self.name} превышает скорость'
        else:
            return f'{self.name} едет с разрешенной скоростью'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость коммерческого авто {self.name} - {self.speed} км/ч')

        if self.speed > 40:
            return f'{self.name} превышает разрешенную для коммерческих авто скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это машина полиции'
        else:
            return f'{self.name} - не полицейская машина'


ferrari = SportCar(100, 'Красный', 'Ferrari', False)
lada = WorkCar(70, 'Белый', 'Lada')
ford = PoliceCar(110, 'Синий',  'Ford', True)
print(lada.turn_left())
print(f'{lada.go()}. {lada.show_speed()}')
print(f'{lada.name} - полицейское авто? {lada.is_police}.')
print(PoliceCar.turn_left(ford))
print(ford.show_speed())