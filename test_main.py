# -*- coding: utf-8 -*-
import unittest
from main import sum_negatives_between_bounds

class TestArraySumNegatives(unittest.TestCase):
    def test_standard_case(self):
        # Максимум = 10 (индекс 1), Минимум = -10 (индекс 5)
        # Между ними элементы: [2, -3, 0] (индексы 2, 3, 4)
        # Отрицательные элементы в промежутке: -3. Сумма = -3.
        arr = [1, 10, 2, -3, 0, -10, 7]
        self.assertEqual(sum_negatives_between_bounds(arr), -3)

    def test_no_elements_between(self):
        # Максимум и минимум стоят вплотную. Элементов между ними нет.
        arr = [1, 10, -10, 5]
        self.assertEqual(sum_negatives_between_bounds(arr), 0)

    def test_no_negatives_between(self):
        # Максимум = 15 (индекс 0), Минимум = -20 (индекс 3)
        # Между ними элементы: [2, 5]. Отрицательных нет.
        arr = [15, 2, 5, -20]
        self.assertEqual(sum_negatives_between_bounds(arr), 0)

    def test_short_array(self):
        # Слишком короткий массив
        self.assertEqual(sum_negatives_between_bounds([5, -5]), 0)

if __name__ == "__main__":
    unittest.main()
