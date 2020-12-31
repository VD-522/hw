# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def task5_1():
    file = open('files/task5_1_txt_file.txt', 'w', encoding='UTF-8')
    def write_to_file():
        txt_line = input('Введите строку для записи в файл или нажмите Enter:\n')
        while True:
            file.writelines(txt_line)
            txt_line = input('Введите строку для записи в файл или нажмите Enter:\n')
            if not txt_line:
                print('Данных для записи нет. Сохраняем и закрываем файл')
                break
        file.write(txt_line + '\n')
        file.close()

    write_to_file()


task5_1()
