# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
#  (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random as r

size = int(input("Введите количество элементов: "))
first_list = [x * r.randint(0, size) for x in range(size)]

# Another way to Check
#first_list = [8, 3, 15, 6, 4, 2, ]

# ---------------Variant1--------------------------
print(f'Вариант1')
second_list_v1 = [i for i, value in enumerate(first_list) if value % 2 == 0]
print(f'Первый список: {first_list}\nВторой массив: {second_list_v1}\n')

# ---------------Variant2--------------------------
print(f'Вариант2')
second_list_v2 = []

for i, value in enumerate(first_list):
    if value % 2 == 0:
        second_list_v2.append(i)

print(f'Первый список: {first_list}\nВторой массив: {second_list_v2}')
