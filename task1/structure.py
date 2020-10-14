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

class ListComparator(list): #Сравнение по длине списка
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

class StrComparator(str): #Сравнение по длине строки
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

class DictComparator(dict): #Сравнение по длине значений словаря
    '''Компаратор для словарей'''
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
