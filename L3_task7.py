# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

import random as r


def search_for_min(random_list):
    min_ = 10000
    index_min = 0

    for i, value in enumerate(random_list):
        if min_ > value:
            min_ = value
            index_min = i

    return min_, index_min


size = int(input("Введите количество элементов: "))
min_item = 0
max_item = 100
random_list = [r.randint(min_item, max_item) for _ in range(size)]

# Another way to Check
#random_list = [2, 2, 5, 6, 7, 8, ]

min_1, index_min = search_for_min(random_list)
random_list.pop(index_min)

min_2, _ = search_for_min(random_list)
random_list.insert(index_min, min_1)

print(f'Cписок:\n {random_list}\n')
print(f'Первый минимальный элемент: {min_1}')
print(f'Второй минимальный элемент: {min_2}\n')
