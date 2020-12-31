# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def task5_5():
    try:
        with open('files/task5_5.txt', 'w') as file:
            line = input('Введите числа через пробел:\n')
            file.writelines(line)
            file.close()
            content = line.split()
            sum_content = sum(map(int, content))
            print(f'Сумма введённых Вами чисел равна {sum_content}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Некорректно введены данные')

task5_5()