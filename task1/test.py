import unittest
import structure
import database
import demo

class Test(unittest.TestCase):
    '''Класс для тестирования программы'''
    
    def test_binary_heap_constructor(self):
        bh = structure.BinaryHeap([1, 2, 3])
        self.assertEqual(bh, [1, 2, 3])

    def test_binary_heap_heapify(self):
        bh = structure.BinaryHeap([4, 3, 2, 4, 4, 3])
        bh.heapify()
        self.assertEqual(bh, [2, 3, 3, 4, 4, 4])

    def test_binary_heap_print(self):
        bh = structure.BinaryHeap([4, 3, 2, 4, 4, 3])
        bh.heapify()
        bh.print()

    def test_binary_heap_check(self):
        bh = structure.BinaryHeap([1, 2, 3])
        self.assertEqual(bh.check(), type(bh))

    def test_binary_heap_pop(self):
        bh = structure.BinaryHeap([4, 3, 2, 4, 4, 3])
        bh.heapify()
        self.assertEqual(bh.pop_(), 2)
        
    def test_binary_heap_push(self):
        bh = structure.BinaryHeap([4, 3, 2, 4, 4, 3])
        bh.heapify()
        bh.push(1)
        self.assertEqual(bh, [1, 3, 2, 4, 4, 4, 3])

    def test_binary_heap_replace(self):
        bh = structure.BinaryHeap([4, 3, 2, 4, 4, 3])
        bh.heapify()
        bh.replace(1)
        self.assertEqual(bh, [1, 3, 3, 4, 4, 4])
    
    def test_list_comparator(self):
        list1 = structure.ListComparator([1, 2, 3])
        list2 = structure.ListComparator([1, 1, 1, 1])
        self.assertTrue(list1 < list2)

    def test_str_comparator(self):
        str1 = structure.StrComparator('abcdefg')
        str2 = structure.StrComparator('aaaaaaa')
        self.assertTrue(str1 == str2)

    def test_dict_comparator(self):
        dict1 = structure.DictComparator({'name': 'Alex', 'age': '767687'})
        dict2 = structure.DictComparator({'name': 'Ivan', 'age': '0'})
        self.assertTrue(dict1 == dict2)

    def test_enter_element_number(self):
        self.assertEqual(database.enter_element_number('Введите число (10, чтобы тест прошел): '), 10)

    def test_create_heap(self):
        tb = database.Table()
        self.assertEqual(tb.create_heap(), ([], 'int'))

    def test_enter_element_list(self):
        tb = database.Table()
        self.assertEqual(tb.enter_element_list(), ["a", "bc", 5])

    def test_enter_element_dict(self):
        tb = database.Table()
        self.assertEqual(tb.enter_element_dict(), {'10': '10', '20': '20'})

    def test_table_push_element(self):
        tb = database.Table()
        tb.push([1, 2, 3])
        tb.push([1])
        self.assertEqual(tb, [[1], [1, 2, 3]])

    def test_table_pop_element(self):
        tb = database.Table()
        tb.push([1, 2, 3])
        tb.push([1])
        self.assertEqual(tb.pop_(), [1])

    def test_table_replace_element(self):
        tb = database.Table()
        tb.push([1, 2, 3])
        tb.push([1])
        tb.replace([2])
        self.assertEqual(tb, [[2], [1,2,3]])

    def test_table_print(self):
        tb = database.Table([1, 2, 3])
        tb.print()

    def test_table_menu(self):
        ui = demo.UserInterface()
        ui.table_menu()

    def test_database_menu(self):
        ui = demo.UserInterface()
        ui.database_menu()
    
if __name__ == 'main':
    unittest.main()
