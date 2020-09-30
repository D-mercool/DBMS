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

def user_interface():
    print('МЕНЮ\n')
    print('1. Создать очередь с приоритетом заполненную псевдослучайными числами.')
    print('2. Создать пустую очередь ')
    print('3. Добавить новый элемент.')
    print('4. Добавить несколько элементов.')
    print('5. Удалить элемент с наивысшем приоритетом.')
    print('6. Заменить элемент (т.е внести новый элемент и удалить элемент с наивысшем приоритетом).')
    print('7. Вывести на экран очередь с приоритетом.')
    print('8. Выйти.')
    print('\n')
    
    queue = []
    t = 'None'
    
    while True:
        number = enter_element_number('Введите номер пункта меню: ',
                                      'Вы ввели не верный номер. Попробуйте еще раз')

        if number == 1:
            queue, t = create_queue()
            flag = True
        elif number == 2:
            queue, t = create_empty_queue()
            flag = True
        elif number == 3:
            wrapper(queue, push_element, t)
        elif number == 4:
            wrapper(queue, push_elements, t)
        elif number == 5:
            wrapper(queue, pop_element, t)
        elif number == 6:
            wrapper(queue, replace_element, t)
        elif number == 7:
            wrapper(queue, print_queue, t)
        elif number == 8: 
            print('До свидания!')
            print(queue)
            break
        else:
            print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

def enter_element_number(text_input,
                         text_except='Вы ввели не число. Попробуйте еще раз...'):
    while True:
        try:
            element = float(input(text_input))
            return element
        except ValueError:
            print(text_except)

def enter_element_list():
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

def wrapper(queue, target, t):  
    if target.__code__.co_argcount == 2:
        target(queue, t)
    else:
        target(queue)

def check_type_wrapper(queue, t, target):
    if t == 'int' or t == 'float':
        element = enter_element_number('Введите число: ')
        if target == 'push':
            queue.push(element)
        elif target == 'replace':
            queue.replace(element)
        print('Элемент успешно добавлен!')
    elif t == 'string':
        element = input('Введите строку: ')
        if target == 'push':
            queue.push(StrComparator(element))
        elif target == 'replace':
            queue.replace(StrComparator(element))
        print('Элемент успешно добавлен!')
    elif t == 'list':
        element = enter_element_list()
        if target == 'push':
            queue.push(ListComparator(element))
        elif target == 'replace':
            queue.replace(ListComparator(element))
        print('Элемент успешно добавлен!')
    
def create_queue():
    size = enter_element_number('\nВведите размер очереди (целое положительно число): ')
    values = get_random_values(size)
        
    queue = PriorityQueue(values)
    queue.heapify()
    print('Очередь с приоритетом имеет вид: ')
    queue.print()
    
    return queue, 'int'

def create_empty_queue():
    while True:
        t = input('Введите какой тип данных хотите хранить' +
                  '\n(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов): ')

        if t == 'float' or t == 'int' or t == 'list' or t == 'string':
            break
        else:
            print('Вы ввели не правильный тип данных, попробуйте еще раз...')
            
    queue = PriorityQueue([])
    queue.heapify()
    print('Очередь с приоритетом имеет вид: ')
    queue.print()
    print('Тип элементов: ' + t)
    
    return queue, t
                 
def push_element(queue, t):
    check_type_wrapper(queue, t, 'push')

def replace_element(queue, t):
    check_type_wrapper(queue, t, 'replace')

def push_elements(queue, t):
    size = enter_element_number('Сколько добавляем элементов?: ')
    [push_element(queue, t) for _ in range(int(size))]

def pop_element(queue):
    if len(queue) > 0:
        element = queue.pop_()
        print(f'\nЭлемент "{element}" успешно удален')
    else:
        print('\nПустая очередь!')

def print_queue(queue):
    queue.print()

def get_random_values(size, minimum = 1, maximum = 100):
    return [random.uniform(minimum, maximum) for _ in range(int(size)) if int(size) > 0 ]


user_interface()
