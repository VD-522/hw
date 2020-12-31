# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
hours_subj = {}
with open('files/task5_6_timetable.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        hours_lst_str = []
        subject, hours_str = line.split(': ')
        # лучшее, что придумал - replace. Возможно ли провести замену, указав список заменяемых на '' элементов?
        hours_values_str0 = hours_str.replace('(л)', '')
        hours_values_str1 = hours_values_str0.replace('(пр)', '')
        hours_values_str2 = hours_values_str1.replace('(пр)', '')
        hours_values_str3 = hours_values_str2.replace('(лаб)', '')
        hours_values_str4 = hours_values_str3.replace('.', '')
        hours_values_str5 = hours_values_str4.replace('—', '0')
        hours_lst_str = hours_values_str5.split()
        hours_lst_int = []
        for el in hours_lst_str:
            el = int(el)
            hours_lst_int.append(el)
        subject_dict = {subject: sum(hours_lst_int)}
        # не хватило сил отыскать, как вывести все элементы в одну строку, надеюсь, не критично :)
        for subj in subject_dict:
            print(f'"{subj}": {subject_dict[subj]}')