# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


# так и не разобрался до конца, как надо
# закомментированное решение - то, которое я пытался сделать сам
# раскомментированное - то, которое я написал по Вашему образцу.
# однако новый ввод данных почему-то замещает исходные (в моём коде примерно то же происходило)
# и не прикрутился индекс, нумерующий кортежи
# p.s. и остались { , } , и кавычки
# не судите строго, на выходных ещё буду с этим разбираться и посмотрю уже целиком Ваше решение :)


# def create_new_tuple_list():
#     print('Собираем данные о новом товаре:')
#     items_set = set()
#     item_name = input("Введите название:\n")
#     items_set.add(item_name)
#     price_set = set()
#     item_price = input("Введите цену:\n")
#     price_set.add(item_price)
#     quantity_set = set()
#     item_q = input("Введите количество:\n")
#     quantity_set.add(item_q)
#     units_set = set()
#     item_u = input("Введите, в каких единицах измеряется количество:\n")
#     units_set.add(item_u)
#
#     def dialogue():
#         dialogue_inp = input('Вы хотите ввести данные о другом типе товаров? (1 - да, 0 - нет)\n')
#         try:
#             if int(dialogue_inp) == 1:
#                 return create_new_tuple_list()
#             else:
#                 print('oк, база сейчас имеет вид:')
#                 print(items_set)
#                 print(price_set)
#                 print(quantity_set)
#                 print(units_set)
#                 print('Приводим к структуре:')
#
#                 goods_tuple = ()
#                 for item_t in items_set:
#                     goods_tuple += items_set, price_set, quantity_set, units_set
#                 print(f'goods_tuple: {goods_tuple}')
#                 obj_types_tuple = ("название", "цена", "количество", "ед")
#                 structure_dict = {}
#                 structure_set = set()
#                 structure_list = []
#                 for i in range(0, len(items_set)):
#                     for el in range(0, len(obj_types_tuple)):
#                         structure_dict[obj_types_tuple[el]] = goods_tuple[el]
#                 print(f'structure_dict: {structure_dict}')
#                 print(len(structure_dict))
#                 for idx, item_l in enumerate(structure_dict):
#                     print(i + 1, item_l)
#
#         except ValueError:
#             print('Ответ не распознан, пожалуйста, повторите')
#             return dialogue()
#
#     dialogue()


def task6():
    # create_new_tuple_list()
    def dialogue():
        products = [
            (1, {'название': 'ПК', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
        ]

        index = 2

        res = {
            'название': set(),
            'цена': set(),
            'количество': set(),
            'ед': set(),
        }
        dialogue_inp = input('Посмотреть аналитику (1) или добавить новый товар (2)?\n')
        if int(dialogue_inp) == 2:
            name, price, count, unit = input("Введите через пробел название, цену, кол-во, ед-цы измерения\n").split()
            products = []
            index = 2
            products.append((
                index,
                {
                    'название': name,
                    'цена': float(price),
                    'количество': int(count),
                    'ед': unit,
                }
            ))
            index += 1
            for product in products:
                res['название'].add(product[1]['название'])
                # поясните, пожалуйста, еще раз запись выше
                res['цена'].add(product[1]['цена'])
                res['количество'].add(product[1]['количество'])
                res['ед'].add(product[1]['ед'])
                print(res)
                return dialogue()

        elif int(dialogue_inp) == 1:
            for product in products:
                res['название'].add(product[1]['название'])
                # поясните, пожалуйста, еще раз запись выше
                res['цена'].add(product[1]['цена'])
                res['количество'].add(product[1]['количество'])
                res['ед'].add(product[1]['ед'])
                print(res)
            return dialogue()

    dialogue()

task6()