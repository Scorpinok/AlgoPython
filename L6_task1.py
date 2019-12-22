# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
#  первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# L3_task2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
#  (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random as r
from collections import deque
import sys


def show_me_size(val):
    a = 0
    b = 0
    a += sys.getsizeof(val)
    if hasattr(val, '__iter__'):
        if hasattr(val, 'items'):
            for value in val.items():
                b += sys.getsizeof(value)
        elif not isinstance(val, str):
            for item in val:
                b += sys.getsizeof(item)
    return a + b


size = int(input("Введите количество элементов: "))
first_list = [x * r.randint(0, size) for x in range(size)]

val_0 = show_me_size(first_list) + show_me_size(size)

# ---------------Вариант1--------------------------
print(f'Вариант1')
second_list_v1 = [i for i, value in enumerate(first_list) if value % 2 == 0]
print(f'Первый список: {first_list}\nВторой список: {second_list_v1}\n')

val_v1 = show_me_size(second_list_v1) + val_0

# ---------------Вариант2--------------------------
print(f'Вариант2')
second_list_v2 = []
val_v2_1 = 0
val_v2_2 = 0

for i, value in enumerate(first_list):
    if value % 2 == 0:
        second_list_v2.append(i, )
    val_v2_1 = show_me_size(value)
    val_v2_2 = show_me_size(i)

print(f'Первый список: {first_list}\nВторой список: {second_list_v2}\n')

val_v2 = show_me_size(second_list_v2) + val_v2_1 + val_v2_2 + val_0

# ---------------Вариант3--------------------------
print(f'Вариант3')
second_list_v3 = deque([])
count_ = 0
val_v3_2 = 0
val_v3_3 = 0
val_v3_4 = 0

for i, value in enumerate(first_list):
    value_div = str(value / 2).split('.')
    if value_div[1] == '0':
        second_list_v3.insert(count_, i)
        count_ += 1
    val_v3_2 = show_me_size(value)
    val_v3_3 = show_me_size(i)
    val_v3_4 = show_me_size(value_div)

val_v3_1 = show_me_size(count_) + val_v3_2 + val_v3_3 + val_v3_4
print(f'Первый список: {first_list}\nВторой список: {second_list_v3}')
val_v3 = show_me_size(second_list_v3) + val_0

print(f'\nРезультаты работы: \nВариант1 {val_v1} байт \nВариант2 {val_v2} байт \nВариант3 {val_v3} байт')

#-----------------------Выводы-----------

#  PyCharm x64, Win10 x64

#Проведена оценка используемой памяти тремя разными реализованными алгоритмами 2го задания 3го урока.
# По результатам оценки можно сделать вывод, о том, что наименее требовательный к памяти
#  вариант реализации алгоритма - Вариант1, а наиболее требовательный - Вариант3. Так случилось потому, что Вариант3
#  использует не только большее количество переменных, но и коллекции, требующие значительных объемов памяти,
#  по сравнению с обычными списками, для реализации результирующего списка.
#Также на объем занимаемой памяти влияют общее количество переменных и размер списка для обработки.