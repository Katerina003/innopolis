import unittest
import random
import main

class TestSortingFunctions(unittest.TestCase):

    def test_bubble_sort(self):
        # Проверка корректности сортировки пузырьком
        input_list = [3, 2, 1, 5, 4]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(main.bubble_sort(input_list), expected_output)

    def test_insertion_sort(self):
        # Проверка корректности сортировки вставками
        input_list = [3, 2, 1, 5, 4]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(main.insertion_sort(input_list), expected_output)

    def test_selection_sort(self):
        # Проверка корректности сортировки выбором
        input_list = [3, 2, 1, 5, 4]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(main.selection_sort(input_list), expected_output)

    def test_sorting_random_lists(self):
        # Проверка корректности сортировки на случайно сгенерированных списках
        input_list = random.sample(range(100), 10)  # Генерация случайного списка длиной 10
        expected_output = sorted(input_list)  # Сортировка списка с использованием встроенной функции sorted
        self.assertEqual(main.bubble_sort(input_list), expected_output)
        self.assertEqual(main.insertion_sort(input_list), expected_output)
        self.assertEqual(main.selection_sort(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
