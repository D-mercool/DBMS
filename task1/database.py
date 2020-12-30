from structure import BinaryHeap, ListComparator, DictComparator, StrComparator

import os
import random
import re
import json

class Table(BinaryHeap): #Таблица условное название (для удобства), это просто бинарная куча
    '''Компаратор для таблиц'''
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return len(self) == len(other)
    
    def enter_element_list(self): #Парсер ввода для элементов списка
        mass = input('Введите список объектов через запятую.' +
                    '\nЕсли хотите записать строку (пример:"ваша_строка")'+
                    '\nЕсли хотите записать число кавычки не нужны.'+
                    '\nЦелые числа пишутся через точку (пример: "a","bc",5.0): ').split(',')
    
        element = []
        for i in mass: 
            if re.findall(r'[0-9]+\.[0-9]+', i) or re.findall(r'"[0-9]+\.[0-9]+"', i): #Числа через точку
                try:
                    element.append(float(i))
                except Exception:
                    element.append(re.findall(r'"[0-9]+\.[0-9]+"', i)[0][1:-1]) #Строка с числом
            elif re.findall(r'"\D+"', i): #Поиск
                try:
                    element.append(re.findall(r'"\D+"', i)[0][1:-1]) #Поиск любых символов кроме цифры
                except Exception:
                    continue
            elif re.findall(r'"\w+"', i):
                try:
                    element.append(re.findall(r'"\w+"', i)[0][1:-1]) #Поиск любой буквы или части слова
                except Exception:
                    continue
            else:
                try:
                    element.append(i[1:-1]) #Если ничего не найдет, то это просто слово
                except Exception:
                    continue
        return element

    def enter_element_dict(self): #Ввод элементов словаря
        size = enter_element_number('\nВведите размер словаря, который хотите внести (целое положительно число): ')  
        while True:
            try:
                element = dict([input('Введите ключ и значение через пробел: ').split() for _ in range(int(size))])
                return element
            except Exception:
                print('Не верное значение! Попробуйте сначала')

    def wrapper(self, element, heap, target, Comparator):
        if target == 'push':
            heap.push(Comparator(element))
            print('Элемент успешно добавлен!')
        elif target == 'replace':
            heap.replace(Comparator(element))
            print('Элемент успешно заменен!')

    def check_type_wrapper(self, heap, t, target): #Проверка на тип данных, в зависимости от этого различный тип ввода
        if t == 'int':
            element = enter_element_number('Введите число: ')
            self.wrapper(element, heap, target, int)
        elif t == 'float':
            element = enter_element_number('Введите число: ')
            self.wrapper(element, heap, target, float)
        elif t == 'string':
            element = input('Введите строку: ')
            self.wrapper(element, heap, target, StrComparator)
        elif t == 'list':
            element = self.enter_element_list()
            self.wrapper(element, heap, target, ListComparator)
        elif t == 'dict':
            element = self.enter_element_dict()
            self.wrapper(element, heap, target, DictComparator)

    def create_heap(self): #создание очереди с указанием типа
        while True:
            t = input('Введите какой тип данных хотите хранить' +
                      '\n(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов, dict:словарь): ')

            if t == 'float' or t == 'int' or t == 'list' or t == 'string' or t == 'dict':
                break
            else:
                print('Вы ввели не верный тип данных, попробуйте еще раз...')
            
        heap = BinaryHeap([])
        heap.heapify()
        print('Таблица имеет вид: ')
        heap.print()
        print('Тип элементов: ' + t)
    
        return heap, t
                 
    def push_element(self, heap, t): #Добавление
        self.check_type_wrapper(heap, t, 'push')
 
    def replace_element(self, heap, t): #Замена
        self.check_type_wrapper(heap, t, 'replace')

    def push_elements(self, heap, t): #Добавление нескольких элементов
        size = enter_element_number('Сколько добавляем элементов?: ')
        [self.push_element(heap, t) for _ in range(int(size))]

    def pop_element(self, heap): #Удаление элементов с наивысшим приоритетом, если очередь не пуста
        if len(heap) > 0:
            element = heap.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая таблица!')

    def print_heap(self, heap): #Вывод очереди
        heap.print()


class Database(BinaryHeap):
    '''Класс для хранения таблиц, тип: бинарная таблица'''
    def create_table(self):
        os.system("cls")
        print('Создание новой таблицы...')
        name_table = input('Введите имя новой таблицы: ')
        table = self.table_menu()
        self.push(DictComparator({name_table: table}))
        os.system("cls")
        self.database_menu()

    def print_table(self):
        print(self)

    def pop_table(self):
        if len(self) > 0:
            element = self.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая база данных!')
            
    def replace_table(self):
        self.pop_table()
        self.create_table()
    
    def save_database(self):
        while True:
            file_name = input('Какая назвать файл с базой данных?: ')
            try:
                f = open(file_name, 'w')  # открытие в режиме записи
                f.write(str(self))
                f.close()
                print('База данных успешно сохранена.')
                break
            except Exception:
                print('\nНеудалось сохранить базу данных')

    def open_database(self):
        while True:
            file_name = input('Введите имя базы данных: ')
            try:
                f = open(file_name, 'r')
                for line in f:
                    db = Database(json.loads(line.replace("'", '"')))
                f.close()
                print('База данных успешно загружена.')
                return db
            except Exception:
                print('\nНеудалось загрузить базу данных')  
        

def enter_element_number(text_input,
                         text_except='Вы ввели не число. Попробуйте еще раз...'): #Функция для ввода чисел
    while True:
        try:
            element = float(input(text_input))
            return element
        except ValueError:
            print(text_except)
