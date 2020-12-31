# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
profit = {}
avg_profit = {}
total_profit = 0
prof_aver = 0
i = 0
with open('files/task5_7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        name, form, income, loss = line.split()
        profit[name] = float(income) - float(loss)
        if profit[name] >= 0:
            total_profit += profit[name]
            i += 1
    if i != 0:
        prof_aver = total_profit / i
        print(f'Средняя прибыль - {prof_aver}')
    else:
        print(f'Фирма работает в убыток')
    # почему, если 'average_profit' написать как "средняя прибыль", выползает следующее:
    # "\u0441\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u0438\u0431\u044b\u043b\u044c": 3500}
    # ведь кодировка указана явно?
    avg_profit = {'average_profit': round(prof_aver)}
    profit.update(avg_profit)
    print(f'Прибыль каждой компании - {profit}')
    file.close()

with open('files/file_7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(profit, json_file)
    json_str = json.dumps(profit)
    print(f'Создан файл json со следующим содержимым: \n '
          f' {json_str}')
    json_file.close()
