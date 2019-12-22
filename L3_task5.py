# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#  Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
#  разных значения.

import random as r

size = int(input("Введите количество элементов: "))
min_item = -100
max_item = 50
random_list = [r.randint(min_item, max_item) for _ in range(size)]

max_ = -10000

index_max = 0

for i, value in enumerate(random_list):
    if value < 0:
        if max_ < value:
            max_ = value
            index_max = i

print(f'Список:\n {random_list}\n')
print(f'Максимальный отрицательный элемент: {max_}, его индекс: {index_max}')
