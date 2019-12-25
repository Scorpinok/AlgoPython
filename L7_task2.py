# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
#  на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random as r


def make_sort_by_merge(array_to_sort):
    if len(array_to_sort) > 1:

        half = len(array_to_sort) // 2

        array_to_sort_1 = array_to_sort[:half]
        array_to_sort_2 = array_to_sort[half:]

        make_sort_by_merge(array_to_sort_1)
        make_sort_by_merge(array_to_sort_2)

        i = 0
        j = 0
        k = 0

        while i < len(array_to_sort_1) and j < len(array_to_sort_2):
            if array_to_sort_1[i] < array_to_sort_2[j]:
                array_to_sort[k] = array_to_sort_1[i]
                i += 1
            else:
                array_to_sort[k] = array_to_sort_2[j]
                j += 1
            k += 1

        while i < len(array_to_sort_1):
            array_to_sort[k] = array_to_sort_1[i]
            i += 1
            k += 1

        while j < len(array_to_sort_2):
            array_to_sort[k] = array_to_sort_2[j]
            j += 1
            k += 1

        return array_to_sort

    elif len(array_to_sort) == 1:
        return array_to_sort


number_ = int(input("Введите колличество элементов списка: "))
start_ = 0
end_ = 49
list_ = [round(r.uniform(start_, end_), 2) for _ in range(number_)]

print(f'\nИсходный список:\n{list_}')
print(f'\nОтсортированный список:\n{make_sort_by_merge(list_)}')
