# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

val1 = float(input("Введите первое число: "))
val2 = float(input("Введите второе число: "))
val3 = float(input("Введите третье число: "))

if val1 > val2:
    if val1 > val3:
        if val2 > val3:
            print(f"Среднее число: {val2}")
        else:
            print(f"Среднее число: {val3}")

if val2 > val3:
    if val2 > val1:
        if val1 > val3:
            print(f"Среднее число: {val1}")
        else:
            print(f"Среднее число: {val3}")

if val3 > val1:
    if val3 > val2:
        if val1 > val2:
            print(f"Среднее число: {val1}")
        else:
            print(f"Среднее число: {val2}")
