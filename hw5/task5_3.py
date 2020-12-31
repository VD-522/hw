# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('files/task5_3_staff.txt', 'r', encoding='UTF-8') as file:
    salaries = []
    small_salaries = []
    content = file.read().split('\n')
    for i in content:
        i = i.split()
        if int(i[1]) < 20000:
           small_salaries.append(i[0])
        salaries.append(i[1])
print(f'Оклад меньше 20.000 {small_salaries}, средняя з.п.: {sum(map(int, salaries)) / len(salaries)}')
file.close()