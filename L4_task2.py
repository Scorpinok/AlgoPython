# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
#  принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость
#  и сложность алгоритмов.

import timeit
import cProfile


# Вариант 1. Эратосфен

s_sieve='''def func_sieve(index_, n=100):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(res[index_ - 1])
    
func_sieve(5)
'''

print(f'Algo func_sieve TIMEIT')
print(timeit.timeit(s_sieve, number=10))

# Среднее время работы
# 0.00039759999999999796

def func_sieve(index_, n=100):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(res[index_ - 1])

print(f'Algo func_sieve cProfile')
cProfile.run('func_sieve(5)')

# 7 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:28(func_sieve)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:29(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:39(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2. Сундарам
s_sundaram='''
def func_sundaram(index_, n=50):
    b = [2, ]
    a = [0] * n

    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0

    for i in range(0, n):
        if a[i] == 0:
            b.append(2 * i + 1)

    print(b[index_ - 1])
    
func_sundaram(5)
'''
print(f'Algo sundaram TIMEIT')
print(timeit.timeit(s_sundaram, number=10))

# Среднее время работы
# 0.00029210000000000347

def func_sundaram(index_, n=50):
    b = [2, ]
    a = [0] * n

    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0

    for i in range(0, n):
        if a[i] == 0:
            b.append(2 * i + 1)

    print(b[index_ - 1])

print(f'Algo sundaram cProfile')
cProfile.run('func_sundaram(5)')

# 29 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:70(func_sundaram)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вариант 3. Перебор делителей
s_perebor='''
def func_perebor(index_, n=100):
    list_ = [i for i in range(n)]
    res_list = []

    for val in range(2, len(list_)):
        i = 2
        j = 0
        while i * i <= list_[val] and j != 1:
            if list_[val] % i == 0:
                j = 1
            i += 1
        else:
            if j != 1:
                res_list.append(list_[val])
    print(res_list[index_ - 1])
    
func_perebor(5)
'''

print(f'Algo perebor TIMEIT')
print(timeit.timeit(s_perebor, number=10))

# Среднее время работы
# 0.0009496000000000088

def func_perebor(index_, n=100):
    list_ = [i for i in range(n)]
    res_list = []

    for val in range(2, len(list_)):
        i = 2
        j = 0
        while i * i <= list_[val] and j != 1:
            if list_[val] % i == 0:
                j = 1
            i += 1
        else:
            if j != 1:
                res_list.append(list_[val])
    print(res_list[index_ - 1])

print(f'Algo perebor cProfile')
cProfile.run('func_perebor(5)')

# 32 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:115(func_perebor)
#         1    0.000    0.000    0.000    0.000 L4_task2.py:116(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Общие выводы:
#По полученным средним данным, о скорости работы, представленных алгоритмов, можно сделать вывод о том,
#  что вариант№3 - алгоритм перебора - самый затратный по времени, остальные, а именно алгоритмы Эратосфена и Сундарама,
#  менее затратны и очень близки по времени работы. Однако алгоритм Сундарама более ресурсоемкий, и в этом смысле
# сопоставим с алгоритмом перебора.