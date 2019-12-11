# 4.. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


def count_el(el, n, step, sum):
    if n > 0:
        sum = sum + el
        el = el / step
        n -= 1
        return count_el(el, n, step, sum)
    else:
        return sum


print(f"Сумма ряда: {count_el(1,int(input('Введите количество элементов: ')),-2,0)}")
