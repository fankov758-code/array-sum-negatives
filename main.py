# -*- coding: utf-8 -*-
"""
Решение задачи: Нахождение суммы отрицательных элементов, 
расположенных между максимальным и минимальным элементами.
"""

def sum_negatives_between_bounds(arr):
    """
    Находит сумму отрицательных элементов, расположенных строго между
    минимальным и максимальным элементами одномерного массива.
    """
    if not arr or len(arr) < 3:
        return 0

    # Находим максимальное и минимальное значения
    max_val = max(arr)
    min_val = min(arr)

    # Находим их индексы (первые вхождения)
    idx_max = arr.index(max_val)
    idx_min = arr.index(min_val)

    # Отыскиваем границы интервала "между" ними
    start_idx = min(idx_max, idx_min) + 1
    end_idx = max(idx_max, idx_min)

    # Суммируем отрицательные элементы в интервале
    negatives_sum = 0
    for i in range(start_idx, end_idx):
        if arr[i] < 0:
            negatives_sum += arr[i]

    return negatives_sum

def main():
    print("=== Анализ элементов одномерного массива ===")
    try:
        raw_input = input("Введите элементы массива через пробел: ").strip()
        if not raw_input:
            print("Массив пуст.")
            return
        
        # Преобразуем строку ввода в список вещественных/целых чисел
        arr = [float(x) for x in raw_input.split()]
        print(f"Входной массив (N={len(arr)}): {arr}")
        
        if len(arr) < 3:
            print("Сумма: 0 (недостаточно элементов для поиска диапазона)")
            return

        result = sum_negatives_between_bounds(arr)
        
        # Форматируем вывод (убираем .0 у целых чисел для красоты)
        formatted_result = int(result) if result.is_integer() else result
        print(f"Сумма отрицательных элементов между min и max: {formatted_result}")
        
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числа через пробел.")

if __name__ == "__main__":
    main(
