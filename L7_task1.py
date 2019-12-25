# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random as r


def make_sort_by_bubble(array_to_sort):
    for i in range(1, len(array_to_sort)):
        for j in range(len(array_to_sort)):
            if array_to_sort[j] < array_to_sort[i]:
                array_to_sort[j], array_to_sort[i] = array_to_sort[i], array_to_sort[j]
    return array_to_sort


number_ = int(input("Введите колличество элементов списка: "))
start_ = -100
end_ = 99
list_ = [r.randrange(start_, end_) for _ in range(number_)]

print(f'\nИсходный список:\n{list_}')
print(f'\nОтсортированный список:\n{make_sort_by_bubble(list_)}')
