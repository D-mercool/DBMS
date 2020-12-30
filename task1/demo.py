from database import Table, Database, enter_element_number

class UserInterface(Table, Database):
    
    def table_menu(self): #Интрефейс для взаимодействия с пользователем
        print('МЕНЮ Таблицы\n')
        print('1. Добавить новый элемент.')
        print('2. Добавить несколько элементов.')
        print('3. Удалить элемент с наивысшем приоритетом.')
        print('5. Заменить элемент (т.е внести новый элемент и удалить элемент с наивысшем приоритетом).')
        print('5. Вывести на экран таблицу.')
        print('6. Выйти\Сохранить.')
        print('\n')
    
        heap, t  = self.create_heap()
    
        while True: #Бесконечный цикл для вызова функций класса
            number = enter_element_number('Введите номер пункта меню(ТАБЛИЦЫ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                self.push_element(heap, t)
            elif number == 2:
                self.push_elements(heap, t)
            elif number == 3:
                self.pop_element(heap)
            elif number == 4:
                self.replace_element(heap, t)
            elif number == 5:
                self.print_heap(heap)
            elif number == 6: #Сохранение
                print('До свидания!')
                return heap
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')
                
    def database_menu(self): #Интерфейс для вызова методов
        print('МЕНЮ Базы данных\n')
        print('1. Создать новую таблицу.')
        print('2. Загрузить базу данных.')
        print('3. Вывести все таблицы базы данных.')
        print('4. Удалить таблицу с наивысшим приоритетом.')
        print('5. Заменить таблицу (заменяет таблицу с наивысшим приоритетом).')
        print('6. Выйти\Сохранить.')
        print('\n')
    
    
        while True:
            number = enter_element_number('Введите номер пункта меню(БАЗА ДАННЫХ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                self.create_table() #Создание и открытие МЕНЮ таблицы
                break
            elif number == 2:
                self = UserInterface(self.open_database())
            elif number == 3:
                self.print_table() #Вывод базы данных
            elif number == 4:
                self.pop_table() #Удаление таблицы
            elif number == 5:
                self.replace_table() #Замена таблицы
                break
            elif number == 6: #Сохранение
                self.save_database()
                print('До свидания.') 
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')
