import random
import os
import re

class PriorityQueue(list):
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

    def shiftdown(self, startpos, pos):
        newitem = self[pos] #Получение элемента данной позиции

        while pos > startpos: #пока данная позиция > статовой
            parentpos = (pos - 1) // 2 #Ищем индекс родителя
            parent = self[parentpos] #Ищем родителя
            if newitem < parent: #Если элемент на данной прозиции меньше родителя, то меняем их местами
                self[pos] = parent #то меняем их местами
                pos = parentpos #обновляем позицию
                continue
            break
        
        self[pos] = newitem #Возвращаем элемент на правильную позицию, если if сработал, если не сработал, то остается на месте

    def shiftup(self, pos):
        endpos = len(self) #Последняя позиция - длина массива
        startpos = pos #Стартовая позиция
        newitem = self[pos] #Получение элемента стартовой позиции
    
        leftpos = 2 * pos + 1 #Проверяем child для позиции
        while leftpos < endpos: #Пока позиция child < длины массива
            rightpos = leftpos + 1

            if rightpos < endpos and self[leftpos] > self[rightpos]: #если не конец, и левое больше правого
                leftpos = rightpos #то правый лист идет вверх
        
            self[pos] = self[leftpos] #Родитель = правому листу, если if выполнилось, и левому листу, если не выполнилось
            pos = leftpos #Позиция = правому листу, если if выполнилось, и левому листу, если не выполнилось
            leftpos = 2 * pos + 1 #Обновляем позицию и если не крайние листы цикл повторяется

        self[pos] = newitem #Возвращаем на правильную позицию место
        self.shiftdown(startpos, pos)

    def heapify(self): #Метод преобразования последовательности в кучу
        n = len(self)
        for i in reversed(range(n//2)):
            self.shiftup(i)
  
    def print(self):
        print(self)

    def check(self):
        return type(self)

    def pop_(self): #Извлечение элемента с наивысшем приоритетом
        lastelt = self.pop()
        if self:
            returnitem = self[0]
            self[0] = lastelt
            self.shiftup(0)
            return returnitem
        return lastelt

    def push(self, item): #Добавление элемента
        self.append(item)
        self.shiftdown(0, len(self)-1)

    def replace(self, item): #Замена элемента (добавлеятся данный item, удаляется элемент с наивысшем приоритетом)
        returnitem = self[0]
        self[0] = item
        self.shiftup(0)
        return returnitem

class ListComparator(list):
    '''Компаратор для списков'''
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

class StrComparator(str):
    '''Компаратор для строк'''
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

class DictComparator(dict):
    '''Компаратор для строк'''
    def __gt__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v > length_o
    def __lt__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v < length_o
    def __ge__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v >= length_o
    def __le__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v <= length_o
    def __eq__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v == length_o


class Table(PriorityQueue):
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
    
    def __init__(self, table_name):
        self.name = table_name
        self.queue = self.user_interface()
        
    def user_interface(self):
        print('МЕНЮ Таблицы\n')
        print('1. Создать очередь с приоритетом заполненную псевдослучайными числами.')
        print('2. Создать пустую очередь.')
        print('3. Добавить новый элемент.')
        print('4. Добавить несколько элементов.')
        print('5. Удалить элемент с наивысшем приоритетом.')
        print('6. Заменить элемент (т.е внести новый элемент и удалить элемент с наивысшем приоритетом).')
        print('7. Вывести на экран очередь с приоритетом.')
        print('8. Выйти\Сохранить.')
        print('\n')
    
        queue = []
        t = 'None'
    
        while True:
            number = enter_element_number('Введите номер пункта меню(ТАБЛИЦЫ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                queue, t = self.create_queue()
            elif number == 2:
                queue, t = self.create_empty_queue()
            elif number == 3:
                self.wrapper(queue, self.push_element, t)
            elif number == 4:
                self.wrapper(queue, self.push_elements, t)
            elif number == 5:
                self.wrapper(queue, self.pop_element, t)
            elif number == 6:
                self.wrapper(queue, self.replace_element, t)
            elif number == 7:
                self.wrapper(queue, self.print_queue, t)
            elif number == 8: #Сохранение
                print('До свидания!')
                return queue
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    def enter_element_list(self):
        mass = input('Введите список объектов через запятую.' +
                    '\nЕсли хотите записать строку (пример:"ваша_строка")'+
                    '\nЕсли хотите записать число кавычки не нужны.'+
                    '\nЦелые числа пишутся через точку (пример: "a","bc",5.0): ').split(',')
    
        element = []
        for i in mass:
            if re.findall(r'[0-9]+\.[0-9]+', i) or re.findall(r'"[0-9]+\.[0-9]+"', i):
                try:
                    element.append(float(i))
                except Exception:
                    element.append(re.findall(r'"[0-9]+\.[0-9]+"', i)[0][1:-1])
            elif re.findall(r'"\D+"', i):
                try:
                    element.append(re.findall(r'"\D+"', i)[0][1:-1])
                except Exception:
                    continue
            elif re.findall(r'"\w+"', i):
                try:
                    element.append(re.findall(r'"\w+"', i)[0][1:-1])
                except Exception:
                    continue
            else:
                try:
                    element.append(i[1:-1])
                except Exception:
                    continue
        return element

    def enter_element_dict(self):
        size = enter_element_number('\nВведите размер словаря, который хотите внести (целое положительно число): ')
        element = dict([input('Введите ключ и значение через пробел:').split() for _ in range(int(size))])
        return element

    def wrapper(self, queue, target, t):  
        if target.__code__.co_argcount == 3:
            target(queue, t)
        else:
            target(queue)

    def check_type_wrapper(self, queue, t, target):
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
    
    def create_queue(self):
        size = enter_element_number('\nВведите размер очереди (целое положительно число): ')
        values = get_random_values(size)
        
        queue = PriorityQueue(values)
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
    
        return queue, 'int'

    def create_empty_queue(self):
        while True:
            t = input('Введите какой тип данных хотите хранить' +
                      '\n(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов, dict:словарь): ')

            if t == 'float' or t == 'int' or t == 'list' or t == 'string' or t == 'dict':
                break
            else:
                print('Вы ввели не правильный тип данных, попробуйте еще раз...')
            
        queue = PriorityQueue([])
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
        print('Тип элементов: ' + t)
    
        return queue, t
                 
    def push_element(self, queue, t):
        self.check_type_wrapper(queue, t, 'push')

    def replace_element(self, queue, t):
        self.check_type_wrapper(queue, t, 'replace')

    def push_elements(self, queue, t):
        size = enter_element_number('Сколько добавляем элементов?: ')
        [self.push_element(queue, t) for _ in range(int(size))]

    def pop_element(self, queue):
        if len(queue) > 0:
            element = queue.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая очередь!')

    def print_queue(self, queue):
        queue.print()


class Database(PriorityQueue):
    def user_interface(self):
        print('МЕНЮ Базы данных\n')
        print('1. Создать новую таблицу.')
        print('2. Вывести имя базы данных.')
        print('3. Вывести все таблицы базы данных.')
        print('4. Удалить таблицу с наивысшим приоритетом.')
        print('5. Заменить таблицу (заменяет таблицу с наивысшим приоритетом).')
        print('6. Выйти\Сохранить.')
        print('\n')
    
    
        while True:
            number = enter_element_number('Введите номер пункта меню(БАЗА ДАННЫХ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                self.create_table()
                break
            elif number == 2:
                self.print_name_db()
            elif number == 3:
                self.print_table()
            elif number == 4:
                self.pop_table()
            elif number == 5:
                self.replace(self.create_table())
            elif number == 6: #Сохранение
                print('До свидания!')
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    def create_table(self):
        os.system("cls")
        print('Создание новой таблицы...')
        name_table = input('Введите имя новой таблицы: ')
        table = Table(name_table)
        self.push(DictComparator({name_table: table.queue}))
        os.system("cls")
        self.user_interface()

    def print_table(self):
        print(self)

    def pop_table(self):
        if len(self.database) > 0:
            element = self.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая база данных!')


def get_random_values(size, minimum = 1, maximum = 100):
    return [random.uniform(minimum, maximum) for _ in range(int(size)) if int(size) > 0]

def create_database():
    while True:
        print('Создание новой базы данных...')
        name_database = input('\nВведите название базы данных без пробелов: ')

        if len(name_database.split(' ')) == 1 and name_database != '':
            break
        else:
            print('Вы ввели недопустимое имя, попробуйте еще раз...')
            
    database = Database(PriorityQueue([]))      
    print('База данных ' + name_database + ' успешно создана!')
    return database, name_database

def enter_element_number(text_input,
                         text_except='Вы ввели не число. Попробуйте еще раз...'):
    while True:
        try:
            element = float(input(text_input))
            return element
        except ValueError:
            print(text_except)
    
if __name__ == '__main__':
    database = Database()
    database.user_interface()
    
    '''
    list_database = []
    
    print('Cписок БАЗ ДАННЫХ\n')
    print('1. Показать весь список баз данных.')
    print('2. Добавить новую базу данных.')
    print('3. Удалить базу данных.')
    print('4. Выйти.')
    print('\n')
    
    while True:
        number = enter_element_number('Введите номер пункта меню: ',
                                      'Вы ввели не верный номер. Попробуйте еще раз')
        if number == 1:
            print(list_database)
        elif number == 2:
            os.system("cls")
            database, name_database = create_database()
            database.user_interface()
            list_database.append(DictComparator({name_database: database}))
            os.system("cls")
        elif number == 3:
            key = input('Введите имя базы данных для удаления: ')
            for i in range(len(list_database)):
                for k, v in list_database[i].items():
                    if k == key:
                        db = list_database.pop(i)
                        print(key + ' успешно удалена!')
                        break
                    
        elif number == 4: #Сохранение
            print('До свидания!')
            break
        else:
            print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    '''
