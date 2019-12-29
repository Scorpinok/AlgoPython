# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

def count_me_under_str(string_in):
    string_ = {}
    n = len(string_in)

    for i in range(n):
        for j in range(1, n + 1):
            el = string_in[i:j]
            if el != '' and len(el) != n:
                string_[el] = string_in.count(el)

    return len(string_), string_


string_ = input("Введите строку: ")
# string_ = 'papa'
# string_ = 'sova'

print(f'Количество подстрок: {count_me_under_str(string_)[0]}')
# print(f'и они такие: {[k for k in count_me_under_str(string_)[1].keys()]}')
