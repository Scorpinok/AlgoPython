# 4. Определить, какое число в массиве встречается чаще всего.

import random as r


def search_for_same(random_list):
    count_value = 1
    repeat_list = [[], [], ]

    for i, value_l1 in enumerate(random_list):
        for j, value_l2 in enumerate(random_list):
            if value_l1 == value_l2 and i != j:
                count_value += 1

        if value_l1 not in repeat_list[0] and count_value != 1:
            repeat_list[0].append(value_l1)
            repeat_list[1].append(count_value)

        count_value = 1

    return repeat_list


size = int(input("Введите количество элементов: "))
min_item = 0
max_item = 100
random_list = [r.randint(min_item, max_item) for _ in range(size)]

# Another way to Check
#random_list = [5, 5, 5, 2, 2, 2, 1, ]
#random_list = [5, 2, 1, ]


print(f'Список: {random_list}\n')

max_ = 0
index_max = 0
repeat_list = search_for_same(random_list)

for i, value in enumerate(repeat_list[1]):
    if max_ < value:
        max_ = value

for i, value in enumerate(repeat_list[1]):
    if max_ == value:
        index_max = i
        message_to_print = 'В списке часто встречается цифра ' + str(repeat_list[0][index_max]) + ' (' + \
                           str(max_) + ' раза)' if max_ == 2 or max_ == 3 or max_ == 4 else \
            'В списке часто встречается цифра ' + str(repeat_list[0][index_max]) + ' (' + str(max_) + ' раз)'
        print(message_to_print)

if max_ == 0:
    message_to_print = 'Цифры в списке не повторяются'
    print(message_to_print)
