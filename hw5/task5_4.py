# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

rus_numerals_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
content_new = []
with open('files/task5_4_src.txt', 'r', encoding='UTF-8') as file_src:
    for i in file_src:
        i = i.split(' ', 1)
        content_new.append(rus_numerals_dict[i[0]] + '  ' + i[1])
file_src.close()
with open('files/task5_4_new.txt', 'w', encoding='UTF-8') as file_new:
    file_new.writelines(content_new)
file_new.close()