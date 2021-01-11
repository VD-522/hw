# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):

        # print(f'Суммируем з.п. {self._income.get('wage')} и премию {self._income.get('bonus')}')
        return f'{sum(self._income.values())}'


try:
    a = Position(input('Введите имя:\n'),
                 input('Введите фамилию:\n'),
                 input('Введите должность:\n'),
                 int(input('Введите з.п. целым числом:\n')),
                 int(input('Введите премию целым числом:\n')))
except ValueError:
    print('Введённые данные неверны, пример работы функции от параметров: '
          'Иван, Иванов, 50000, 20000')
    a = Position('Иван', 'Иванов', 'Программист', 100000, 20000)


print(a.get_full_name())
print(a.position)
print(a.get_total_income())