# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class NotEventException(Exception):
    def __init__(self, txt):
        self.txt = txt


def runner_division():
    inp_args = input('Введите делимое и делитель через пробел или введите q для завершения: ')
    print('Проверка...')
    try:
        if inp_args.count(' ') == 1 and len(inp_args.split(' ')) == 2:
            division_args = inp_args.split(' ')
            divisible = int(division_args[0])
            divider = int(division_args[1])
            quotient = divisible / divider
            return quotient

        elif inp_args == 'q':
            exit()
        else:
            raise NotEventException('Ошибка. Проверьте количество параметров и синтаксис.')

    except Exception or NotEventException as err1:
        print(f'Ошибка ввода: {err1}')
        return runner_division()


print(runner_division())
