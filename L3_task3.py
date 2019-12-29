# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as r

size = int(input("Введите количество элементов: "))
min_item = 0
max_item = 100
random_list = [r.randint(min_item, max_item) for _ in range(size)]

max_ = 0
min_ = 10000

index_max = 0
index_min = 0

print(f'Исходный список:\n {random_list}\n')

for i, value in enumerate(random_list):
    if max_ < value:
        max_ = value
        index_max = i

    if min_ > value:
        min_ = value
        index_min = i

random_list[index_max], random_list[index_min] = min_, max_

print(f'Элементы подлежащие взаимной перестановке:')
print(f'Максимальный элемент: {max_}, его индекс: {index_max}')
print(f'Минимальный элемент: {min_}, его индекс: {index_min}\n')

print(f'Измененный список:\n {random_list}')
