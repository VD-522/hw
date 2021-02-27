# 1. Реализовать класс «Дата», функция-конструктор которая
# должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime as dt


def runner_chk_date():
    day_month_year = input('Введите дату в формате день-месяц-год или введите q для завершения: ')
    print('Проверка:')
    try:
        if day_month_year.count('-') == 2:
            # ??? and len(day_month_year.split('-') == 2:
            date_list = day_month_year.split('-')
            day = date_list[0]
            month = date_list[1]
            year = date_list[2]
            d = Date()
            print(d.method_date_into_int(day, month, year))
            print(d.method_check_date(day, month, year))

        elif day_month_year == 'q':
            exit()
        else:
            print('Ошибка ввода, пожалуйста, повторите')
            runner_chk_date()

    except Exception as err1:
        print(f'Ошибка ввода: {err1}')
        return runner_chk_date()

    finally:
        print('Конец скрипта')

class Date:
    @classmethod
    def method_date_into_int(cls, day, month, year):
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            # для ясности возвращаем переменные вместе с их типами:
            return day, type(day), month, type(month), year, type(year)
        except Exception as err2:
            return f'Ошибочка', err2

    @staticmethod
    def method_check_date(day, month, year):
        try:
            if int(year) > dt.now().year:
                year = dt.now().year
                month = dt.now().month
                day = dt.now().day
                print(f'Ошибка указанной даты, дата изменена на сегодняшню.')

            if int(day) < 1 or int(day) > 31:
                day = 1
                print(f'Ошибка в дне указанной даты, значение дня изменено на: {day}.')

            if 1 < int(month) > 12:
                month = 1
                print(f'Ошибка в месяце указанной даты, значение месяца изменено на: {month}.')

        except Exception as err3:
            print(f'Ошибка: {err3}')

        finally:
            print(f'Сейчас дата имеет вид:')
            return day, month, year


runner_chk_date()
