# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#  Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

x = 5
y = 6

x_and_y = x & y
x_or_y = x | y
x_xor_y = x ^ y
x_not = ~ x

x_l_shift = x << 2
x_r_shift = x >> 2

print(f'Участвующие в вычислениях числа: {x}, {y}')
print(f"Результат логических операций над числами:\n"
      f" AND: {x_and_y}\n OR: {x_or_y}\n XOR: {x_xor_y}\n NOT: {x_not}\n")

print(f"Результаты побитовых сдвигов числа {x} вправо и влево на два знака:\n"
      f" Сдвиг влево: {x_l_shift}\n Сдвиг вправо: {x_r_shift}")
