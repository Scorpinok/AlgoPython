# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Использована 4я задача 2го урока:
# L2_task4.py
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

# Вариант 1.  Реализация алгоритма рекурсией
# timeit
s = '''def count_el(el, n, step, sum_):
    if n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
        return count_el(el, n, step, sum_)
    else:
        return sum_

count_el(1,5,-2,0)     #-----    5
#count_el(1,10,-2,0)    #-----    10
#count_el(1,20,-2,0)    #-----    20
#count_el(1,40,-2,0)    #-----    40
#count_el(1,80,-2,0)    #-----    80
'''

# 0.01916240000000001     #-----    5
# 0.02525050000000001     #-----    10
# 0.0515449               #-----    20
# 0.1062749               #-----    40
# 0.2055804               #-----    80

print(f'Algo RECURS TIMEIT')
print(timeit.timeit(s, number=10000))


# cProfile
def count_el(el, n, step, sum_):
    if n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
        return count_el(el, n, step, sum_)
    else:
        return sum_


print(f'Algo RECURS cProfile')
# cProfile.run('count_el(1,5,-2,0)')  # 6/1    0.000    0.000    0.000    0.000 L4_task1.py:36(count_el)
# cProfile.run('count_el(1,10,-2,0)') # 11/1    0.000    0.000    0.000    0.000 L4_task1.py:36(count_el)
# cProfile.run('count_el(1,20,-2,0)') # 21/1    0.000    0.000    0.000    0.000 L4_task1.py:36(count_el)
# cProfile.run('count_el(1,40,-2,0)') # 41/1    0.000    0.000    0.000    0.000 L4_task1.py:36(count_el)
# cProfile.run('count_el(1,80,-2,0)') # 81/1    0.000    0.000    0.000    0.000 L4_task1.py:36(count_el)


# Вариант 2.  Реализация алгоритма циклом while
# timeit
s_cycle = '''def count_el_cycle(el, n, step, sum_):
    while n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
    else:
        return sum_

count_el_cycle(1,5,-2,0)     #-----    5
#count_el_cycle(1,10,-2,0)    #-----    10
#count_el_cycle(1,20,-2,0)    #-----    20
#count_el_cycle(1,40,-2,0)    #-----    40
#count_el_cycle(1,80,-2,0)    #-----    80

'''
# 0.009034799999999982      #-----    5
# 0.014842300000000003      #-----    10
# 0.0283389                 #-----    20
# 0.0558341                 #-----    40
# 0.10280689999999998       #-----    80

print(f'Algo WHILE TIMEIT')
print(timeit.timeit(s_cycle, number=10000))


# cProfile
def count_el_cycle(el, n, step, sum_):
    while n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
    else:
        return sum_


print(f'Algo WHILE cProfile')
# cProfile.run('count_el_cycle(1,5,-2,0)')  #  1    0.000    0.000    0.000    0.000 L4_task1.py:78(count_el_cycle)
# cProfile.run('count_el_cycle(1,10,-2,0)') #  1    0.000    0.000    0.000    0.000 L4_task1.py:78(count_el_cycle)
# cProfile.run('count_el_cycle(1,20,-2,0)') #  1    0.000    0.000    0.000    0.000 L4_task1.py:78(count_el_cycle)
# cProfile.run('count_el_cycle(1,40,-2,0)') #  1    0.000    0.000    0.000    0.000 L4_task1.py:78(count_el_cycle)
# cProfile.run('count_el_cycle(1,80,-2,0)') #  1    0.000    0.000    0.000    0.000 L4_task1.py:78(count_el_cycle)


# Вариант 3.  Реализация алгоритма циклом for
# timeit

s_for = '''
def count_el_for(n,el,sum_,step):        
    for _ in range (n):
        sum_ = sum_ + el
        el = el / step
    return sum_


#count_el_for(5,1,0,-2)  #-----    5
#count_el_for(10,1,0,-2) #-----    10
#count_el_for(20,1,0,-2) #-----    20
#count_el_for(40,1,0,-2) #-----    40
count_el_for(80,1,0,-2) #-----    80

'''
print(f'Algo FOR TIMEIT')
print(timeit.timeit(s_for, number=10000))


# 0.010024099999999994   #-----    5
# 0.01219350000000001    #-----    10
# 0.02172819999999999    #-----    20
# 0.038006700000000004   #-----    40
# 0.07428300000000002   #-----    80

# cProfile
def count_el_for(n, el, sum_, step):
    for _ in range(n):
        sum_ = sum_ + el
        el = el / step
    return sum_


print(f'Algo FOR cProfile')

cProfile.run('count_el_for(5, 1, 0, -2)')  # -----    5
cProfile.run('count_el_for(10, 1, 0, -2)')  # -----    10
cProfile.run('count_el_for(20, 1, 0, -2)')  # -----    20
cProfile.run('count_el_for(40, 1, 0, -2)')  # -----    40
cProfile.run('count_el_for(80, 1, 0, -2)')  # -----    80

# Для всех пяти случаев, сообщение было одно и тоже:
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 L4_task1.py:126(count_el_for)


# Вариант 4.  Применение к алгоритму мемоизации, однако в данном случае это не имеет смысла.
# timeit

s_meme = """
class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result
        
@memoize
def count_el_mem(el, n, step, sum_):
    if n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
        return count_el_mem(el, n, step, sum_)
    else:
        return sum_

#count_el_mem(1,5,-2,0)     #-----    5
#count_el_mem(1,10,-2,0)    #-----    10
#count_el_mem(1,20,-2,0)    #-----    20
#count_el_mem(1,40,-2,0)    #-----    40
count_el_mem(1,80,-2,0)    #-----    80

"""
print(timeit.timeit(s_meme, number=10000))


# 0.1597542              #-----    5
# 0.17560189999999998    #-----    10
# 0.3215343              #-----    20
# 0.6455399              #-----    40
# 0.9413254999999999     #-----    80

# cProfile
class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


@memoize
def count_el_mem(el, n, step, sum_):
    if n > 0:
        sum_ = sum_ + el
        el = el / step
        n -= 1
        return count_el_mem(el, n, step, sum_)
    else:
        return sum_


cProfile.run('count_el_mem(1,5,-2,0)')  # -----    5
# 21 function calls (6 primitive calls) in 0.000 seconds
#       6/1    0.000    0.000    0.000    0.000 L4_task1.py:211(__call__)
#       6/1    0.000    0.000    0.000    0.000 L4_task1.py:214(__missing__)
#       6/1    0.000    0.000    0.000    0.000 L4_task1.py:219(count_el_mem)

cProfile.run('count_el_mem(1,10,-2,0)')  # -----    10
# 36 function calls (6 primitive calls) in 0.000 seconds
#      11/1    0.000    0.000    0.000    0.000 L4_task1.py:211(__call__)
#      11/1    0.000    0.000    0.000    0.000 L4_task1.py:214(__missing__)
#      11/1    0.000    0.000    0.000    0.000 L4_task1.py:219(count_el_mem)

cProfile.run('count_el_mem(1,20,-2,0)')  # -----    20
# 66 function calls (6 primitive calls) in 0.000 seconds
#      21/1    0.000    0.000    0.000    0.000 L4_task1.py:211(__call__)
#      21/1    0.000    0.000    0.000    0.000 L4_task1.py:214(__missing__)
#      21/1    0.000    0.000    0.000    0.000 L4_task1.py:219(count_el_mem)

cProfile.run('count_el_mem(1,40,-2,0)')  # -----    40
#  126 function calls (6 primitive calls) in 0.000 seconds
#      41/1    0.000    0.000    0.000    0.000 L4_task1.py:211(__call__)
#      41/1    0.000    0.000    0.000    0.000 L4_task1.py:214(__missing__)
#      41/1    0.000    0.000    0.000    0.000 L4_task1.py:219(count_el_mem)

cProfile.run('count_el_mem(1,80,-2,0)')  # -----    80
# 246 function calls (6 primitive calls) in 0.001 seconds
#      81/1    0.000    0.000    0.000    0.000 L4_task1.py:211(__call__)
#      81/1    0.000    0.000    0.000    0.000 L4_task1.py:214(__missing__)
#      81/1    0.000    0.000    0.000    0.000 L4_task1.py:219(count_el_mem)


# Общие выводы:
# При реализации алгоритма тремя разными способами, а именно рекурсией, с помощью while и с помощью for
# установлено, что наиболее затраный по времени работы способ - рекурсивный, а менее затратный - с использованием
# цикла for. Так алгоритм с while работает примерно в два раза быстрее чем рекурсивный, а алгоритм с for примерно на 30%
# быстрее чем алгоритм c while.
# Это связано с тем, что рекурсивный метод требует нескольких вызовов функции, что приводит к затратам ресурсов,
# в то время как, алгоритмы реализованные с помощью циклов не требуют многократного вызова. Также следует отметить,
#  что алгоритм, реализованный с помощью цикла for не требует явного подсчета количества оставшихся шагов, в отличии
# от цикла while, что является преимуществом и проявляется самым коротким временем работы среди представленных алгоримтов.
# На основании изложенного самым оптимальным алгоритмом, в данном случае,
# является вариант№3 - реализация алгоритма с помощью цикла for.

# В задании так же приведен пример некорректного применения метода оптимизации - мемоизации, который
#  в данном случае только увеличил время работы, для демонстрации того, что оптимизация может не оказать желаемого
# эффекта.
