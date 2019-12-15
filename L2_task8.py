# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


num_val = int(input("Введите количество вводимых чисел: "))
val = int(input("Введите цифру (0-9) для подсчета: "))

count = 0

while num_val > 0:
    value = input("Введите число: ")
    for i in value:
        if int(i) == val:
            count += 1
    num_val -= 1

string_to_print = 'Цифра встретилась ' + str(count) + ' раза' if count == 2 or count == 3 or count == 4 else \
    'Цифра встретилась ' + str(count) + ' раз'

print(string_to_print)
