# -*- coding: utf-8 -*-
"""
Модуль вычисления суммы отрицательных элементов массива,
расположенных строго между максимальным и минимальным элементами.
"""


def sum_negatives_between_bounds(arr):
    """
    Вычисляет сумму отрицательных элементов, расположенных строго между
    минимальным и максимальным элементами одномерного числового массива.
    
    Параметры:
        arr (list): Одномерный список числовых значений.
        
    Возвращает:
        float/int: Сумма отрицательных элементов диапазона либо 0.
    """
    if not arr or len(arr) < 3:
        return 0

    # Нахождение глобальных экстремумов
    max_val = max(arr)
    min_val = min(arr)

    # Нахождение индексов первых вхождений экстремумов
    idx_max = arr.index(max_val)
    idx_min = arr.index(min_val)

    # Определение динамических границ диапазона поиска
    start_idx = min(idx_max, idx_min) + 1
    end_idx = max(idx_max, idx_min)

    # Итеративное суммирование отрицательных элементов
    negatives_sum = 0
    for i in range(start_idx, end_idx):
        if arr[i] < 0:
            negatives_sum += arr[i]

    return negatives_sum


def main():
    """
    Функция организации консольного пользовательского интерфейса.
    Обеспечивает ввод, синтаксический анализ и обработку исключений.
    """
    print("=== Анализ элементов одномерного массива ===")
    try:
        raw_input_data = input("Введите элементы массива через пробел: ").strip()
        if not raw_input_data:
            print("Массив пуст.")
            return

        # Парсинг строкового ввода в числовой список
        arr = [float(x) for x in raw_input_data.split()]
        print(f"Входной массив (N={len(arr)}): {arr}")

        if len(arr) < 3:
            print("Сумма: 0 (недостаточно элементов для поиска диапазона)")
            return

        result = sum_negatives_between_bounds(arr)

        # Форматирование отображения целых значений
        formatted_result = int(result) if isinstance(result, float) and result.is_integer() else result
        print(f"Сумма отрицательных элементов между min и max: {formatted_result}")

    except ValueError:
        print("Ошибка: Входные данные должны содержать исключительно числа, разделенные пробелами.")


if __name__ == "__main__":
    main()

