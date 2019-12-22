# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

import random as r

size = int(input("Введите количество элементов: "))
min_item = 0
max_item = 100
random_list = [r.randint(min_item, max_item) for _ in range(size)]

max_ = 0
min_ = size * 100

index_max = 0
index_min = 0

print(f'Cписок:\n {random_list}\n')

for i, value in enumerate(random_list):
    if max_ < value:
        max_ = value
        index_max = i

    if min_ > value:
        min_ = value
        index_min = i

print(f'Максимальный элемент: {max_}, его индекс: {index_max}')
print(f'Минимальный элемент: {min_}, его индекс: {index_min}\n')


def sum_list_func(list, index_max, index_min):
    sum_ = 0
    for i in range(index_min, index_max - 1):
        if index_max - index_max <= 1:
            sum_ = sum_ + list[i + 1]
    return sum_ if sum_ != 0 else 'Между числами нет элементов!'


if index_max > index_min:
    print(f'Сумма элементов между минимальным и максимальным элементами:\n '
          f'{sum_list_func(random_list, index_max, index_min)}')
else:
    print(f'Сумма элементов между максимальным и минимальным элементами:\n '
          f'{sum_list_func(random_list, index_min, index_max)}')
