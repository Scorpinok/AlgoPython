# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


size_row = 5  # int(input("Введите количество строк матрицы: "))
size_col = 3  # int(input("Введите количество столбцов матрицы: "))
min_item = 0
max_item = 100

random_matrix = [[int(j) for j in input("Введите три элемента матрицы через пробел:").split()] for _ in range(size_row)]

# Don't want to print, use this:
# import random as r
# random_matrix = [[r.randint(min_item, max_item) for _ in range(size_col)] for _ in range(size_row)]

sum_ = 0
for j in range(size_row):
    for i in range(size_col):
        sum_ = sum_ + random_matrix[j][i]
    random_matrix[j].extend([sum_], )
    sum_ = 0

matrix_col_size = len(random_matrix[0])

print(f'\nМатрица:\n')
for j in range(size_row):
    for i in range(matrix_col_size):
        print(f'{random_matrix[j][i]}', end=' | ')
    print(f'')
