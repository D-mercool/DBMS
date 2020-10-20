from structure import BinaryTree, ListComparator, DictComparator, StrComparator
import os
import random
import re

class Table(BinaryTree): #Таблица условное название (для удобства), это просто очередь с приоритетом
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
                    element.append(re.findall(r'"[0-9]+\.[0-9]+"', i)[0][1:-1]) #Стркоа с числом
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

    def wrapper(self, queue, target, t): #Оболочка для вызова функций 
        if target.__code__.co_argcount == 3: #Если 3 аргумента функции
            target(queue, t)
        else:
            target(queue) #Если не 3 аргумента у функции

    def check_type_wrapper(self, queue, t, target): #Проверка на тип данных, в зависимости от этого различный тип ввода
        if t == 'int' or t == 'float':
            element = enter_element_number('Введите число: ')
            if target == 'push':
                queue.push(element)
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(element)
                print('Элемент успешно заменен!')
        elif t == 'string':
            element = input('Введите строку: ')
            if target == 'push':
                queue.push(StrComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(StrComparator(element))
                print('Элемент успешно добавлен!')
        elif t == 'list':
            element = self.enter_element_list()
            if target == 'push':
                queue.push(ListComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(ListComparator(element))
                print('Элемент успешно добавлен!')
        elif t == 'dict':
            element = self.enter_element_dict()
            if target == 'push':
                queue.push(DictComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(DictComparator(element))
                print('Элемент успешно добавлен!')
    
    def create_queue(self): #Создание очереди с рандомными числами
        size = enter_element_number('\nВведите размер очереди (целое положительно число): ')
        values = get_random_values(size)
        
        queue = BinaryTree(values)
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
    
        return queue, 'int'

    def create_empty_queue(self): #создание очереди с указанием типа
        while True:
            t = input('Введите какой тип данных хотите хранить' +
                      '\n(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов, dict:словарь): ')

            if t == 'float' or t == 'int' or t == 'list' or t == 'string' or t == 'dict':
                break
            else:
                print('Вы ввели не правильный тип данных, попробуйте еще раз...')
            
        queue = BinaryTree([])
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
        print('Тип элементов: ' + t)
    
        return queue, t
                 
    def push_element(self, queue, t): #Добавление
        self.check_type_wrapper(queue, t, 'push')
 
    def replace_element(self, queue, t): #Замена
        self.check_type_wrapper(queue, t, 'replace')

    def push_elements(self, queue, t): #Добавление нескольких элементов
        size = enter_element_number('Сколько добавляем элементов?: ')
        [self.push_element(queue, t) for _ in range(int(size))]

    def pop_element(self, queue): #Удаление элементов с наивысшим приоритетом, если очередь не пуста
        if len(queue) > 0:
            element = queue.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая очередь!')

    def print_queue(self, queue): #Вывод очереди
        queue.print()


class Database(BinaryTree):
    '''Класс для хранения таблиц, тип: очередь с приоритетом'''
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


def get_random_values(size, minimum = 1, maximum = 100): #Получение случайных чисел 0..100
    return [random.uniform(minimum, maximum) for _ in range(int(size)) if int(size) > 0]

def enter_element_number(text_input,
                         text_except='Вы ввели не число. Попробуйте еще раз...'): #Функция для ввода чисел
    while True:
        try:
            element = float(input(text_input))
            return element
        except ValueError:
            print(text_except)
