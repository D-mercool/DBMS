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
    while True:
        number = enter_element('Введите номер пункта меню: ',
                               'Введенного номера нет в МЕНЮ. Попробуйте еще раз.',
                               'Вы ввели не верный номер. Попробуйте еще раз')

        if number == 1:
            queue = create_queue()
        elif number == 2:
            queue = create_empty_queue()
        elif number == 3:
            wrapper(queue, push_element)
        elif number == 4:
            wrapper(queue, push_elements)
        elif number == 5:
            wrapper(queue, pop_element)
        elif number == 6:
            wrapper(queue, replace_element)
        elif number == 7:
            wrapper(queue, print_queue)
        elif number == 8: 
            print('До свидания!')
            return queue
            break
        else:
            print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

def enter_element(text_input,
                  text_else='Введённое число не соответствует заданному диапазону. Попробуйте еще раз...',
                  text_except='Вы ввели не целое число. Попробуйте еще раз...'):
    while True:
        try:
            element = int(input(text_input))
            if 0 < element:
                return element
            else:
                print(text_else)
        except ValueError:
            print(text_except)

def wrapper(queue, target):
  if queue == 'None':
    print('\nОчерь не создана! Создайте очередь с приоритетом.')
  else:
    target(queue)

def create_queue():
    size = enter_element('\nВведите размер очереди (целое положительно число): ')
    values = get_random_values(size)
    
    queue = PriorityQueue(values)
    queue.heapify()
    print('Очередь с приоритетом имеет вид: ')
    queue.print()
    
    return queue

def create_empty_queue():
    queue = PriorityQueue([])
    print('Очередь с приоритетом имеет вид: ')
    queue.print()

    return queue

def push_element(queue):
    element = enter_element('Введите целое положительное число: ')
    queue.push(element)
    print('Элемент успешно добавлен!')

def pop_element(queue):
    if len(queue.heap) > 0:
        element = queue.pop()
        print(f'\nЭлемент "{element}" успешно удален')
    else:
        print('\nПустая очередь!')

def replace_element(queue):
    element = enter_element('Введите целове положительное число: ')
    queue.replace(element)
    print('Элемент успешно добавлен!')
    
def push_elements(queue):
    size = enter_element('Сколько добавляем элементов?: ')
    [push_element(queue) for _ in range(size)]

def print_queue(queue):
    queue.print()

def get_random_values(size, minimum = 1, maximum = 100):
    return [random.randint(minimum, maximum) for _ in range(size)]

queue = user_interface()
