from database import Table, Database, enter_element_number

class UserInterface(Table, Database):
    
    def table_menu(self): #Интрефейс для взаимодействия с пользователем
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
    
        tree = [] #Нужны для проверки на пустоту
        t = 'None'
    
        while True: #Бесконечный цикл для вызова функций класса
            number = enter_element_number('Введите номер пункта меню(ТАБЛИЦЫ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                tree, t = self.create_tree() #Создание таблицы заполненное рандомными числами
            elif number == 2:
                tree, t = self.create_empty_tree() #Создать пустую таблицу с выбором типа данных
            elif number == 3:
                self.wrapper(tree, self.push_element, t) #Добавить 1 элемент
            elif number == 4:
                self.wrapper(tree, self.push_elements, t) #Добавить несколько элементов
            elif number == 5:
                self.wrapper(tree, self.pop_element, t) #Удалить элемент с наивысшим приоритетом
            elif number == 6:
                self.wrapper(tree, self.replace_element, t) #Заменить элемент с наивысшим приоритетом
            elif number == 7:
                self.wrapper(tree, self.print_tree, t) # Вывести таблицу(очередь)
            elif number == 8: #Сохранение
                print('До свидания!')
                return tree
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
                self.create_table() #Создание очереди с приоритетом
                break
            elif number == 2:
                name = input('ВВедите имя базы данных: ')
                print('База данных успешно загружена.')
                self = UserInterface(self.open_database(name + '.txt'))
            elif number == 3:
                self.print_table() #Вывод базы данных
            elif number == 4:
                self.pop_table() #Удаление таблицы
            elif number == 5:
                self.replace_table() #Замена таблицы
                break
            elif number == 6: #Сохранение
                name = input('Какая назвать файл с базой данных: ')
                print('До свидания!')
                self.save_database(name + '.txt')
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')
