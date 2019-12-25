# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#  которые не меньше медианы, в другой — не больше медианы.
import random as r

number_ = 2 * int(input("Введите натуральное число: ")) + 1
start_ = 0
end_ = 100
list_ = [r.randrange(start_, end_) for _ in range(number_)]

print(f'\nИсходный список:\n{list_}')


# ------------------------------ Вариант1 с использованием сортировки --------------------
# ----------------------- функция глупой сортировки -----------------
def make_sort_by_stupid(array_to_sort, i=0):
    n = len(array_to_sort) - 1
    if i < n:
        if array_to_sort[i + 1] < array_to_sort[i]:
            array_to_sort[i], array_to_sort[i + 1] = array_to_sort[i + 1], array_to_sort[i]
            i = 0
            return make_sort_by_stupid(array_to_sort, i)
        else:
            i += 1
            return make_sort_by_stupid(array_to_sort, i)

    return array_to_sort

print(f'\nВариант1\nМедиана списка: \n{make_sort_by_stupid(list_)[len(list_) // 2]}')


# ------------------------------ Вариант2 без использования сортировки -------------------
# ----------------------- функция быстрого выбора -----------------
def fast_choice(list_, half, pivot_rand=r.choice):
    if len(list_) == 1:
        return list_[0]

    pivot = pivot_rand(list_)

    lows = [i for i in list_ if i < pivot]
    highs = [i for i in list_ if i > pivot]
    pivots = [i for i in list_ if i == pivot]

    if half < len(lows):
        return fast_choice(lows, half, pivot_rand)
    elif half < len(lows) + len(pivots):
        return pivots[0]
    else:
        return fast_choice(highs, half - len(lows) - len(pivots), pivot_rand)


half = len(list_) / 2
print(f'\nВариант2\nМедиана списка (без сортировки):\n{fast_choice(list_, half)}')
