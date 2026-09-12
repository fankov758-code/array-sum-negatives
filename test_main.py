# -*- coding: utf-8 -*-
"""
Модуль проведения автоматизированного модульного тестирования
вычислительной функции sum_negatives_between_bounds.
"""

import unittest
from main import sum_negatives_between_bounds


class TestArraySumNegatives(unittest.TestCase):
    """
    Тестовый набор для верификации граничных и стандартных условий работы алгоритма.
    """

    def test_standard_case(self):
        """Тестирование стандартной последовательности с отрицательными элементами."""
        arr = [1, 10, 2, -3, 0, -10, 7]
        self.assertEqual(sum_negatives_between_bounds(arr), -3)

    def test_no_elements_between(self):
        """Тестирование случая соседнего расположения минимума и максимума."""
        arr = [1, 10, -10, 5]
        self.assertEqual(sum_negatives_between_bounds(arr), 0)

    def test_no_negatives_between(self):
        """Тестирование случая отсутствия отрицательных чисел в интервале."""
        arr = [15, 2, 5, -20]
        self.assertEqual(sum_negatives_between_bounds(arr), 0)

    def test_short_array(self):
        """Тестирование обработки массивов с длиной менее 3 элементов."""
        self.assertEqual(sum_negatives_between_bounds([5, -5]), 0)
        self.assertEqual(sum_negatives_between_bounds([10]), 0)
        self.assertEqual(sum_negatives_between_bounds([]), 0)

    def test_reversed_bounds(self):
        """Тестирование случая, когда минимум предшествует максимуму."""
        arr = [-20, 4, -2, -8, 50]
        self.assertEqual(sum_negatives_between_bounds(arr), -10)


if __name__ == "__main__":
    unittest.main()
