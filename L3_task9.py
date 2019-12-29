# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random as r

size_row = int(input("Введите количество строк матрицы: "))
size_col = int(input("Введите количество столбцов матрицы: "))
min_item = 0
max_item = 100
random_matrix = [[r.randint(min_item, max_item) for _ in range(size_col)] for _ in range(size_row)]

matrix_col_size = len(random_matrix[0])
matrix_row_size = len(random_matrix)

print(f'\nСгенерированная матрица:\n')
for j in range(matrix_row_size):
    for i in range(matrix_col_size):
        print(f'{random_matrix[j][i]}', end=' | ')
    print(f'')

max_ = 0
min_ = 10000
min_el_list = []

for i in range(matrix_col_size):
    for j in range(matrix_row_size):
        if min_ > random_matrix[j][i]:
            min_ = random_matrix[j][i]
            index_min = i
    min_el_list.append(min_)
    min_ = 10000

for value in min_el_list:
    if max_ < value:
        max_ = value

print(f'\nМаксимальный элемент среди минимальных элементов столбцов:\n {max_}')
