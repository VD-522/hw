# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.
file = open('files/task5_2_text_file.txt', 'r', encoding = 'UTF-8')
content = file.read()
print(f'Содержимое файла:\n{content}')
file = open('files/task5_2_text_file.txt', 'r')
content = file.readlines()
print(f'\nКоличество строк в файле - {len(content)}')
file = open('files/task5_2_text_file.txt', 'r')
content = file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
# странно он считает слова: 19 ведь ответ, Word полагает, что 20. У него 21.
file.close()