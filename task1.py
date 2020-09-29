import random
import os

class PriorityQueue():
    def __init__(self, queue):
        self.heap = queue

    def shiftdown(self, startpos, pos):
        newitem = self.heap[pos] #Получение элемента данной позиции

        while pos > startpos: #пока данная позиция > статовой
            parentpos = (pos - 1) // 2 #Ищем индекс родителя
            parent = self.heap[parentpos] #Ищем родителя
            if newitem < parent: #Если элемент на данной прозиции меньше родителя, то меняем их местами
                self.heap[pos] = parent #то меняем их местами
                pos = parentpos #обновляем позицию
                continue
            break
        
        self.heap[pos] = newitem #Возвращаем элемент на правильную позицию, если if сработал, если не сработал, то остается на месте

    def shiftup(self, pos):
        endpos = len(self.heap) #Последняя позиция - длина массива
        startpos = pos #Стартовая позиция
        newitem = self.heap[pos] #Получение элемента стартовой позиции
    
        leftpos = 2 * pos + 1 #Проверяем child для позиции
        while leftpos < endpos: #Пока позиция child < длины массива
            rightpos = leftpos + 1

            if rightpos < endpos and self.heap[leftpos] > self.heap[rightpos]: #если не конец, и левое больше правого
                leftpos = rightpos #то правый лист идет вверх
        
            self.heap[pos] = self.heap[leftpos] #Родитель = правому листу, если if выполнилось, и левому листу, если не выполнилось
            pos = leftpos #Позиция = правому листу, если if выполнилось, и левому листу, если не выполнилось
            leftpos = 2 * pos + 1 #Обновляем позицию и если не крайние листы цикл повторяется

        self.heap[pos] = newitem #Возвращаем на правильную позицию место
        self.shiftdown(startpos, pos)

    def heapify(self): #Метод преобразования последовательности в кучу
        n = len(self.heap)
        for i in reversed(range(n//2)):
            self.shiftup(i)
  
    def print(self):
        print(self.heap)

    def check(self):
        return type(self.heap)

    def pop(self): #Извлечение элемента с наивысшем приоритетом
        lastelt = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self.shiftup(0)
            return returnitem
        return lastelt

    def push(self, item): #Добавление элемента
        self.heap.append(item)
        self.shiftdown(0, len(self.heap)-1)

    def replace(self, item): #Замена элемента (добавлеятся данный item, удаляется элемент с наивысшем приоритетом)
        returnitem = self.heap[0]
        self.heap[0] = item
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
    
    queue = 'None'
    t = 'None'
    
    while True:
        number = enter_element_number('Введите номер пункта меню: ',
                                      'Вы ввели не верный номер. Попробуйте еще раз')

        if number == 1:
            queue, t = create_queue()
        elif number == 2:
            queue, t = create_empty_queue()
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
            return queue
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

def wrapper(queue, target, t):
    if queue == 'None':
        print('\nОчерь не создана! Создайте очередь с приоритетом.')   
    else:
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
        element = input('Введите список объектов: ')
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
                  '(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов): ')

        if t == 'float' or t == 'int' or t == 'list' or t == 'string':
            queue = PriorityQueue([])
            print('Очередь с приоритетом имеет вид: ')
            queue.print()
            print('Тип элементов: ' + t)
            return queue, t
        else:
            print('Вы ввели не правильный тип данных, попробуйте еще раз...')
            
def push_element(queue, t):
    check_type_wrapper(queue, t, 'push')

def replace_element(queue, t):
    check_type_wrapper(queue, t, 'replace')

def pop_element(queue):
    if len(queue.heap) > 0:
        element = queue.pop()
        print(f'\nЭлемент "{element}" успешно удален')
    else:
        print('\nПустая очередь!')
    
def push_elements(queue, t):
    size = enter_element_number('Сколько добавляем элементов?: ')
    [push_element(queue, t) for _ in range(int(size))]

def print_queue(queue):
    queue.print()

def get_random_values(size, minimum = 1, maximum = 100):
    return [random.uniform(minimum, maximum) for _ in range(int(size)) if int(size) > 0 ]

queue = user_interface()
