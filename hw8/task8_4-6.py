# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь."""
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

from datetime import datetime as dt


class InvalidException(Exception):
    def __init__(self, param):
        print(f'>> Сработало исключение:')
        print(f'>> Недопустимое значение')
        self.txt = param
        once_again()


class Warehouse:
    warehouse_dict: dict = {}
    # к вопросу ниже (см. запуск демо-режима) - если импортировать словарь через json, по идее ведь его потом надо
    # экспортировать? 6_6  Как бы это лучше сделать? ^_^

    # ?: отчего если словари объявлять здесь, а не в подклассах оборудования,
    # начинается бред с перезаписью:
    # eq_type_dict: dict = {}
    # tmp_dict: dict = {}
    def __init__(self):
        # ?: и начинается бред, если словари объявлять здесь, а не в подклассах оборудования
        # self.warehouse_dict = {}
        # self.eq_type_dict: dict = {}
        pass

    def add_item(self, equipment):
        # equipment = переданный аргумент от класса Equip, вызванного подклассом Printer/Scanner/Etc(Equip)
        """ добавляем в словарь обьект по его названию, в значении будет список экземпляров этого оборудования"""
        print('\n>> Добавляется:')
        print(f'{equipment.eq_type}, инв.№ {equipment.counter}, данные: {equipment}')
        """ ?: (к предыдущему вопросу) и здесь не удалось нормально объявить словари (с этого, собственно, начал):
        # self.tmp_dict: dict = {}
        # tmp_dict[equipment.counter] = equipment
        """
        """
        # проверка, что же во временном словаре подкласса Printer/.../Etc(Equip):
        print(f'tmp_dict:!!!!!!!!!!!!')
        # print(type(equipment.__class__.tmp_dict))
        print(equipment.__class__.tmp_dict)

        # проверка, что же сейчас в словаре подкласса Printer/.../Etc(Equip):
        # print(f'eq_type_dict:*********')
        # print(type(equipment.__class__.eq_type_dict))
        # print(equipment.__class__.eq_type_dict)
        """
        # добавляем в словарь tmp_dict подкласса Printer/.../Etc(Equip) счётчик и словарь repr_dict того же подкласса:
        equipment.__class__.tmp_dict.setdefault(equipment.counter, equipment.repr_dict)
        # в словарь eq_type_dict добавляем в раздел, соотв. классу оборуд-я словарь tmp подкласса Printer/.../Etc(Equip)
        equipment.__class__.eq_type_dict.update(equipment.__class__.tmp_dict)
        # в подраздел подкласса Printer/...Etc{Equip) складского словаря добавляем словарь eq_type_dict
        self.__class__.warehouse_dict[equipment.eq_type] = equipment.__class__.eq_type_dict
        """# print('------- Текущее состояние склада --------')
        print(self.__class__.warehouse_dict)"""
        # проверка, что же сейчас в основном словаре каждого подкласса Printer/.../Etc(Equip):
        # print(f'eq_type_dict:+++++++++++++++')
        # print(equipment.__class__.eq_type_dict)
        # print(type(equipment.__class__.eq_type_dict))
        print(f'>> Оборудование {equipment.eq_type}, инв. № {equipment.counter} успешно добавлено\n')
        # проверка, что же сейчас в складском словаре
        # print(type(self.warehouse_dict))
        # print(self.warehouse_dict)
        # # вычищаем временный словарь подкласса Printer/.../Etc(Equip)
        equipment.__class__.tmp_dict.clear()

    def extract(self, eq_type):
        """ удаляем из словаря обьект по названию группы и инв. номеру. """
        """ переписав комментарии и добавив вывод денег в отдельную структуру, можно адаптировать метод для продажи"""
        print(f'сейчас на складе следующее оборудование типа {eq_type}: ')
        print(str(self.warehouse_dict[eq_type]))
        try:
            inv_no = int(input('укажите инв. номер удаляемого со склада оборудования:\n'
                               '---> '))
            if self.warehouse_dict[eq_type]:
                print('>> Удаляется:')
                print(self.warehouse_dict.setdefault(eq_type)[inv_no])
                self.warehouse_dict.setdefault(eq_type).pop(inv_no)
        except Exception as wronginv:
            print(f'>> Ошибка удаления')
            print(wronginv)

    # def assign_to_dept(self, eq_type, inv_no, dept):     # это была первая идея, как реализовать метод
    def assign_to_dept(self, equipm):
        print(f'\nСейчас на складе следующее нераспределённое оборудование типа {equipm.eq_type}: ')
        print(self.__class__.warehouse_dict[equipm.eq_type])
        inv_no = int(input('Укажите инв. номер оборудования, которое необходимо передать структуре:\n'
                           '---> '))
        dept = input('Укажите структуру для передачи оборудования:\n'
                     '---> ')
        item = self.__class__.warehouse_dict[equipm.eq_type][inv_no]
        # item = dict(item)
        # print(type(item))
        # print(item)
        # item = equipm.__class__.eq_type_dict[inv_no]
        item['ассоциирован'] = dept
        if dept != '':
            print(f'>> Устройство успешно ассоциировано с указанной структурой:')
            print(item)
        else:
            print(f'>> Ошибка установки ассоциаций. Имя структуры не может быть пустым.\n')
            item.department = None

    def arrange_eq_type_by_dept(self, equip_cls):
        flag = True
        try:
            filter_dept = input('\nАссоциации с какими структурами Вас интересуют? \n'
                                '---> ')
            print(f'>> Поиск оборудования закреплённого за структурой "{filter_dept}":')
            eq_type_dict_to_filter = self.__class__.warehouse_dict[equip_cls.eq_type]
            # print(f'ищем в словаре из следующих позиций:')
            # print(type(eq_type_dict_to_filter))
            # print(eq_type_dict_to_filter)
            for i in eq_type_dict_to_filter:
                if eq_type_dict_to_filter[i].get('ассоциирован').upper() == filter_dept.upper():
                    print(eq_type_dict_to_filter[i])
                    # ?: почему по yield возвращается объект-генератор, а не значение?
                    flag = False

            def show_all_eq_for_dept():
                print(f'Отобразить оборудование всех типов, ассоциированное с данной структурой / отделом?')
                question_input = input('1 - Да, 0 - Нет\n'
                                       '---> ')
                if int(question_input) == 1:
                    wrh_dict_to_filter = self.__class__.warehouse_dict
                    for eqtype in wrh_dict_to_filter:
                        for invnum in wrh_dict_to_filter[eqtype]:
                            if wrh_dict_to_filter[eqtype][invnum].get('ассоциирован').upper() == filter_dept.upper():
                                print(wrh_dict_to_filter[eqtype][invnum])
                                # flag = False
                    return f'>> Поиск завершён. Выходим в главное меню'
                elif int(question_input) == 0:
                    pass
                else:
                    print(f'>> Ответ не распознан. Выходим в главное меню.')
                    interface_menu()
                return f''

            if flag:
                search_err_str = f'>> Не найдено оборудование, ассоциированное с данной структурой.'
                return search_err_str
            print(f'>> Поиск завершён')
            return show_all_eq_for_dept()
        except InvalidException as wrong_dept:
            print(wrong_dept)


"""end of Warehouse Block"""


##########################################################################################################
##########################################################################################################

class Equip:
    def __init__(
            self,
            vendor: str,
            model: str,
            # думал сначала проверять переданные аргументы здесь, но впоследствии сделал проверку в меню интерфейса
            useful_economic_life: int,
            # надо бы по-хорошему проверять дату на формат, чтобы возвращать подробное инфо при ошибке ввода
            purchase_date: str,
            purchase_price: float
    ):

        self.vendor = vendor
        self.model = model
        self.uel = useful_economic_life
        # валидация даты покупки:
        try:
            self.p_date = dt.strptime(purchase_date, '%d-%m-%Y')
            if self.p_date > dt.today():
                print(f'Ошибка. Пожалуйста, вводите реальную дату в формате дд-мм-гггг.')
                InvalidException(Exception)
                interface_menu()
        except ValueError as val_err:
            print(val_err)
            print(f'Ошибка. Пожалуйста, вводите дату в формате дд-мм-гггг.')
            print(f'>> Возврат в главное меню.')
            interface_menu()
        self.p_price = purchase_price
        self.eq_type = self.__class__.__name__
        self.department = None

    def eq_type(self):
        return f'{self.eq_type}'

    @property
    def economic_life_left(self):
        today = dt.today()
        economic_life_left = self.uel - (today.year - self.p_date.year) * 12 + (today.month - self.p_date.month)
        return economic_life_left

    @property
    # recommended retail price = rrc
    def recommended_retail_price(self):
        """ vat = НДС """
        vat = 0.20
        # если захочется целевую прибыль сделать динамической
        # retail_rate = float(input('целевая наценка, десятичное число: '))
        retail_rate = 1.3
        """ yr_depreciation = годовая амортизация """
        yr_depreciation: float
        # rrc: float = 0
        if 40000 < self.p_price < 100000:
            yr_depreciation = self.p_price / self.uel * 12
        elif self.p_price > 100000:
            """вторая амортизационная группа, срок амортизации 24-36 мес.:"""
            yr_depreciation = self.p_price / 24 * 12
        else:
            yr_depreciation = 0

        if yr_depreciation == 0:
            if self.economic_life_left < 0:
                econ_life_left = -self.economic_life_left
                rrc = (self.p_price - self.p_price / econ_life_left) * retail_rate * (1 + vat)
            else:
                rrc = (self.p_price - self.p_price / self.economic_life_left) * retail_rate * (1 + vat)
        else:
            rrc = self.p_price - yr_depreciation * retail_rate * (1 + vat)

        return round(rrc, 2)

    @property
    def dept_string(self):
        dept_string = self.department
        if dept_string is None:
            dept_string = f'доступен для ассоциации'
        else:
            dept_string = f'{self.department}'
        return dept_string

    @property
    def about_ec_life_left_str(self):
        expiry = f'ост_службы'
        if self.economic_life_left < 0:
            ec_life_left = -self.economic_life_left
            over = f'сверх_'
            # логика проверки даты - добавить символы ?..!, если логика нарушена, и оборудование старше 20 лет:
            if ec_life_left > 240:
                ec_life_left = str(ec_life_left).join('?!')
            about_ec_life_left_str = f'{over}{expiry}: {ec_life_left}'
        else:
            about_ec_life_left_str = f'{expiry}: {self.economic_life_left}'
        return about_ec_life_left_str

    @property
    def repr_dict(self):
        repr_dict = {'vendor': self.vendor, 'модель': self.model, 'куплен': self.p_date.strftime("%d-%m-%Y"),
                     'срок': self.about_ec_life_left_str, 'цена закупки': self.p_price,
                     'РРЦ': self.recommended_retail_price,
                     'ассоциирован': self.dept_string}
        return repr_dict

    def __repr__(self):
        # return f'{self.vendor}, ' \
        #        f'модель: {self.model}, ' \
        #        f' куплен: {self.p_date.strftime("%d-%m-%Y")}, ' \
        #        f'{about_ec_life_left_str} мес., ' \
        #        f'цена закупки: {self.p_price}, ' \
        #        f'РРЦ: {self.recommended_retail_price}, ' \
        #        f'{self.dept_string}, ' \
        #        f'\n'
        """ изменил структуру на словарь для поиска по ключам """
        # ?: есть вопрос по способу ниже (нашёл в интернете: https://riptutorial.com/python/example/17080/motivation)
        # ?: почему здесь для задания переменной в методе get указывается только первый параметр. Ведь могут быть другие
        # позиции с тем же названием, в данном случае, вендора?
        repr_string = self.repr_dict.get(self.vendor, str(self.vendor))
        repr_string_formatted = "vendor: %s, модель: %s, куплен: %s, мес_%s, закуп.цена: %s, РРЦ: %s, " \
                                "ассоциации: %s \n" % (repr_string, self.model, self.p_date.strftime("%d-%m-%Y"),
                                                       self.about_ec_life_left_str, self.p_price,
                                                       self.recommended_retail_price, self.dept_string)
        return repr_string_formatted


"""end of Equipment Block"""


##########################################################################################################
##########################################################################################################


class Printer(Equip):
    counter = 0
    eq_type_dict: dict = {}
    tmp_dict: dict = {}

    def __init__(self, vendor, model, useful_economic_life, purchase_date, purchase_price):
        self.can_print = 1      # три данных свойства по идее надо выделять через @property или типа того,
        self.can_scan = 0       # но свойства нигде больше не используются, хотя при расширении функционала
        self.can_copy = 0       # интерфейса можно их использовать для фильтрации, например, только печатающих устр-в.
        self.__class__.counter += 1
        self.eq_type_dict: dict = {}
        super().__init__(vendor, model, useful_economic_life, purchase_date, purchase_price)


class Scanner(Equip):
    counter = 0
    eq_type_dict: dict = {}
    tmp_dict: dict = {}

    def __init__(self, vendor, model, useful_economic_life, purchase_date, purchase_price):
        self.can_print = 0
        self.can_scan = 1
        self.can_copy = 0
        self.__class__.counter += 1
        self.eq_type_dict: dict = {}
        super().__init__(vendor, model, useful_economic_life, purchase_date, purchase_price)


class Xerox(Equip):
    counter = 0
    eq_type_dict: dict = {}
    tmp_dict: dict = {}

    def __init__(self, vendor, model, useful_economic_life, purchase_date, purchase_price):
        self.can_print = 0
        self.can_scan = 0
        self.can_copy = 1
        self.__class__.counter += 1
        self.eq_type_dict: dict = {}
        super().__init__(vendor, model, useful_economic_life, purchase_date, purchase_price)


class MFD(Equip):
    counter = 0
    eq_type_dict: dict = {}
    tmp_dict: dict = {}

    def __init__(self, vendor, model, useful_economic_life, purchase_date, purchase_price):
        self.can_print = 1
        self.can_scan = 1
        self.can_copy = 1
        self.__class__.counter += 1
        self.eq_type_dict: dict = {}
        super().__init__(vendor, model, useful_economic_life, purchase_date, purchase_price)


"""*****************************************************************************************************************"""
if __name__ == '__main__':
    print(f'\n>> НАЧАЛО РАБОТЫ МОДУЛЯ В ДЕМО-РЕЖИМЕ <<')
    print(f' формируется первоначальный склад ')
    # наверное, в идеале, хотя бы подтягивать файл json, но, честно говоря, не вполне был уверен в реализации
    # был бы признатен за наводку, как это лучше реализовывать

    # создаем объект
    warehouse = Warehouse()

    # добавляем оборудование на склад: vendor, model, uel, p_date, p_price

    scanner = Scanner('scan_hp', 'mod1', 90, '01-02-2020', 39000.5)
    warehouse.add_item(scanner)

    printer = Printer('prin_ricoh', 'mod1', 60, '20-08-2015', 45000.5)
    warehouse.add_item(printer)

    printer = Printer('prin_kyocera', 'mod2', 60, '20-02-2015', 45000.5)
    warehouse.add_item(printer)
    # print('------- Текущее состояние склада: -----------')
    # print(warehouse.warehouse_dict)

    # print('Добавим сканер, а то сканеры иногда стирали строки в принтерах!')
    scanner = Scanner('scan_hp', 'mod2', 90, '20-02-2018', 40000.5)
    warehouse.add_item(scanner)
    # print('------- Текущее состояние склада: -----------')
    # print(warehouse.warehouse_dict)

    # print('\n-------Теперь списываем со склада принтер-------')
    # warehouse.extract('Printer')
    # print(warehouse.warehouse_dict)

    # print('И ещё добавим другой сканер')
    scanner = Scanner('scan_canon', 'mod3', 90, '20-02-2016', 99000.5)
    warehouse.add_item(scanner)

    # print('------- Текущее состояние склада: -----------')
    # print(warehouse.warehouse_dict)

    # print('И ещё добавим 1 принтер')
    printer = Printer('prin-hp', 'mod3', 90, '20-02-2017', 99000.5)
    warehouse.add_item(printer)

    # print('------- Текущее состояние склада: -----------')
    # print(warehouse.warehouse_dict)

    """здесь дико непонятный глюк: закрепить оборудование за отделом удаётся только если вызывать метод с параметром
    с маленькой буквы (или же, в добавлении принтера выше: >>И ещё добавим 1 принтер<< надо менять
    Printer = Printer(...)
    warehouse.add_item(Printer), но т.к. это не по фен-шуй, долго бился над ошибкой
    KeyError: <function Equip.eq_type at 0x034FA850>, пока не сменил в методе ниже параметр на маленькую букву:
    было >> warehouse.assign_to_dept(Printer)
    стало >> warehouse.assign_to_dept(printer)"""
    # print('\nЗакрепляем принтер за отделом / структурой:')
    # warehouse.assign_to_dept(printer)
    #
    # print('\nЗакрепляем сканер за отделом / структурой:')
    # warehouse.assign_to_dept(scanner)

    """additional equipment block"""
    # print('Добавим также ксерокс:')
    xerox = Xerox('copier_Xerox', 'mod1', 36, '20-02-2017', 10000.5)
    warehouse.add_item(xerox)

    # print('И добавим МФУ:')
    mfd = MFD('mfd_Epson', 'mod1', 36, '01-01-2018', 45000.5)
    warehouse.add_item(mfd)
    """"end of additional equipment block"""

    # print('------- Текущее состояние склада: -----------')
    # print(warehouse.warehouse_dict)

    # print('------- Этот метод определяет, какие принтеры закреплены за определённой структурой: -----------')
    # print(warehouse.arrange_eq_type_by_dept(printer))

    print(f'\n >> ФОРМИРОВАНИЕ ПЕРВИЧНОГО СКЛАДА ЗАВЕРШЕНО. КОНЕЦ РАБОТЫ МОДУЛЯ В ДЕМО-РЕЖИМЕ <<')


    class InputException(Exception):
        def __init__(self, param):
            print(param)
            print(f'>> Недопустимое значение')
            interface_menu()

    def once_again():
        y_or_n = input(f'Попробовать еще раз? Да - Y / Нет - N\n'
                       f'---> ')
        if y_or_n.upper() == 'Y':
            return interface_menu()
        elif y_or_n.upper() == 'N' or y_or_n == '':
            print(f'>> Скрипт завершён, но были ошибки ввода. Спасибо за внимание :)')
            exit()
        else:
            print(f'>> Ответ не распознан')
            return once_again()

    def interface_menu():
        print('\n------- Текущее состояние склада: -----------')
        wrh = warehouse.warehouse_dict
        print(wrh)
        prn_dict_len = len(wrh['Printer'])
        scn_dict_len = len(wrh['Scanner'])
        xer_dict_len = len(wrh['Xerox'])
        mfd_dict_len = len(wrh['MFD'])
        wrh_dict_len = prn_dict_len + scn_dict_len + xer_dict_len + mfd_dict_len
        print(f'На складе {wrh_dict_len} устройств, из них:')
        print(f'принтеров: {prn_dict_len};')
        print(f'сканеров: {scn_dict_len};')
        print(f'ксероксов: {xer_dict_len};')
        print(f'МФУ: {mfd_dict_len}.')

        def main_menu():
            print(f'\nМЕНЮ:')
            print(f'1. добавить оборудование на склад')
            print(f'2. удалить оборудование со склада')
            print(f'3. закрепить / открепить оборудование за структурой / отделом')
            print(f'4. отобразить оборудование, закреплённое (ассоциированное) за структурой / отделом')
            print(f'5. Выход')

        def print_equipment_type_menu():
            print(f'ВЫБЕРИТЕ ТИП ОБОРУДОВАНИЯ:')
            print(f'1. Принтер')
            print(f'2. Сканер')
            print(f'3. Ксерокс')
            print(f'4. МФУ')
            print(f'5. Отмена')

        def conditions(param):
            if not param.isdigit():
                raise InputException(Exception)
            elif int(param) < 1 or int(param) > 5:
                raise InputException(Exception)
            else:
                pass

        try:
            main_menu()
            menu = (input('Выберите пункт меню и нажмите Enter: \n'
                          '---> '))
            conditions(menu)
            if int(menu) == 1:  # добавить
                def add_equipment():
                    print(f'\nДобавление оборудования.')
                    print_equipment_type_menu()
                    select_equip_type = (input('Выберите пункт меню и нажмите Enter: \n'
                                               '---> '))
                    conditions(select_equip_type)
                    # добавляем оборудование на склад: vendor, model, uel, p_date, p_price
                    print(f'Укажите через пробел 5 параметров по следующему образцу:\n'
                          f'Производитель Модель Срок_годности(мес.) Дата_покупки_через_дефис Цена\n'
                          f'Пример:\n'
                          f'>> |vendor|  model   |uel|purchased|price|\n'
                          f'>>  Canon Laserjet210 36 01-01-2010 30000')
                    try:
                        properties_string = input('Введите через пробел параметры оборудования\n'
                                                  '---> ')
                        eq_params = properties_string.split()
                        if len(eq_params) != 5:
                            print(f'>> Ошибка в количестве параметров. Необходимо вводить 5 через пробел.')
                            raise InputException(eq_params)     # consider #

                        eq_params = properties_string.split()
                        if int(select_equip_type) == 1:  # принтер
                            # printer_new = Printer('printer_Samsung', 'mod5', 36, '20-02-2017', 35000.5)
                            try:
                                printer_new = Printer(eq_params[0], eq_params[1], int(eq_params[2]), eq_params[3],
                                                      float(eq_params[4]))
                                warehouse.add_item(printer_new)
                            except ValueError as inp_exception:     # почему здесь не срабатвает именное исключение
                                print(inp_exception)                # например, InputException?
                                print(f'Ошибка в параметрах. Нужно 5 параметров: строка, строка, число, '
                                      f'дата(дд-мм-гггг), десятичное число.')
                                interface_menu()
                                once_again()
                        elif int(select_equip_type) == 2:  # сканер1
                            scanner_new = Scanner(eq_params[0], eq_params[1], int(eq_params[2]), eq_params[3],
                                                  float(eq_params[4]))
                            warehouse.add_item(scanner_new)
                            interface_menu()
                        elif int(select_equip_type) == 3:  # ксерокс
                            xerox_new = Xerox(eq_params[0], eq_params[1], int(eq_params[2]), eq_params[3],
                                              float(eq_params[4]))
                            warehouse.add_item(xerox_new)
                            interface_menu()
                        elif int(select_equip_type) == 4:  # МФУ
                            mfd_new = MFD(eq_params[0], eq_params[1], int(eq_params[2]), eq_params[3],
                                          float(eq_params[4]))
                            warehouse.add_item(mfd_new)
                            interface_menu()
                        elif int(select_equip_type) == 5:  # отмена
                            interface_menu()
                    except InputException as oou:
                        print(oou)

                add_equipment()
                interface_menu()
                pass
            elif int(menu) == 2:  # удалить
                try:
                    def extr_equipent():
                        print(f'\n>> Удаление оборудования.')
                        print_equipment_type_menu()
                        select_extr_eq_type = (input('Выберите пункт меню и нажмите Enter: \n'
                                                     '---> '))
                        conditions(select_extr_eq_type)
                        if int(select_extr_eq_type) == 1:  # принтер
                            warehouse.extract('Printer')
                        elif int(select_extr_eq_type) == 2:  # сканер
                            warehouse.extract('Scanner')
                        elif int(select_extr_eq_type) == 3:  # ксерокс
                            warehouse.extract('Xerox')
                        elif int(select_extr_eq_type) == 4:  # МФУ
                            warehouse.extract('MFD')
                        elif int(select_extr_eq_type) == 5:  # отмена
                            interface_menu()

                    extr_equipent()
                    interface_menu()
                except InputException as extr_err:
                    print(extr_err)
                    interface_menu()

            elif int(menu) == 3:  # закрепить
                def assign_to_dept_menu():
                    print(f'\nЗакрепление (ассоциация) оборудования за отделом / структурой.')
                    print_equipment_type_menu()
                    select_eq_type_to_assign = (input('Выберите пункт меню и нажмите Enter: \n'
                                                      '---> '))
                    conditions(select_eq_type_to_assign)
                    # выбор ниже повторяется несколько раз. по идее, можно выввести в отдельную функцию
                    if int(select_eq_type_to_assign) == 1:  # принтер
                        warehouse.assign_to_dept(printer)
                    elif int(select_eq_type_to_assign) == 2:  # сканер
                        warehouse.assign_to_dept(scanner)
                    elif int(select_eq_type_to_assign) == 3:  # ксерокс
                        warehouse.assign_to_dept(xerox)
                    elif int(select_eq_type_to_assign) == 4:  # МФУ
                        warehouse.assign_to_dept(mfd)
                    elif int(select_eq_type_to_assign) == 5:  # отмена
                        interface_menu()

                assign_to_dept_menu()
                interface_menu()

            elif int(menu) == 4:  # фильтровать
                print(f'Фильтр оборудования, закрепленного за определённой структурой / отделом')
                print_equipment_type_menu()
                select_eq_type = (input('Выберите пункт меню и нажмите Enter: \n'
                                        '---> '))
                conditions(select_eq_type)
                if int(select_eq_type) == 1:  # принтер
                    print(warehouse.arrange_eq_type_by_dept(printer))
                elif int(select_eq_type) == 2:  # сканер
                    print(warehouse.arrange_eq_type_by_dept(scanner))
                elif int(select_eq_type) == 3:  # ксерокс
                    print(warehouse.arrange_eq_type_by_dept(xerox))
                elif int(select_eq_type) == 4:  # МФУ
                    print(warehouse.arrange_eq_type_by_dept(mfd))
                elif int(select_eq_type) == 5:  # отмена
                    interface_menu()
                interface_menu()
            elif int(menu) == 5:  # отмена
                print(f'Скрипт успешно завершён. :)')
                print(f'Текущее состояние склада:\n{wrh}')
                exit()

        except InputException:
            print(f'>> Были ошибки ввода')
            once_again()


    interface_menu()
