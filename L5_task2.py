# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
# их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
#  произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def is_it_number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def define_letter(letter_f):
    res = letter_f
    if is_it_number(res):
        return res
    else:
        if ord(letter_f) >= 97 and ord(letter_f) <= 102:
            res = ord(letter_f) - 87
        if ord(letter_f) >= 65 and ord(letter_f) <= 70:
            res = ord(letter_f) - 55
        return res


def to_char(a, b):
    return int(str(a) + str(b))


def sign_plus_sign(letter_f, letter_s):
    if not is_it_number(letter_f) and not is_it_number(letter_s):
        res = define_letter(letter_f) + define_letter(letter_s)
    elif is_it_number(letter_f) and not is_it_number(letter_s):
        res = int(letter_f) + define_letter(letter_s)
    elif not is_it_number(letter_f) and is_it_number(letter_s):
        res = define_letter(letter_f) + int(letter_s)
    else:
        res = int(letter_f) + int(letter_s)
        if res <= 9:
            return res

    if res > 15:
        res -= 16
        if res <= 9:
            return 1, res
        else:
            return 1, chr(55 + res)
    else:
        return chr(55 + res)


def mult_func(first_dig_deq, second_dig_deq):
    string_ = "( ) , ' "
    alter_dig = first_dig_deq
    other_dig = 0
    for k in range(int(second_dig_deq) - 1):
        res = deque(str(sign_plus_sign(alter_dig, first_dig_deq)))
        if len(res) > 1:
            res.reverse()
            for j in range(len(res)):
                if res[j] not in string_ and res[j] != '1':
                    alter_dig = res[j]
                if res[j] == '1':
                    other_dig += 1
        else:
            alter_dig = res[0]
            if i == int(second_dig_deq) - 1:
                other_dig = 0
    return str(other_dig), alter_dig


def add_func(first_dig_deq, second_dig_deq, other_dig):
    res_dig_deq = deque()
    if len(first_dig_deq) > len(second_dig_deq):
        n = len(first_dig_deq)
        for _ in range(len(first_dig_deq) - len(second_dig_deq)):
            second_dig_deq.extendleft('0')
    else:
        n = len(second_dig_deq)
        for _ in range(len(second_dig_deq) - len(first_dig_deq)):
            first_dig_deq.extendleft('0')

    first_dig_deq.reverse()
    second_dig_deq.reverse()
    string_ = "( ) , ' "
    flag = 0
    for i in range(n):
        plus_in_mind = sign_plus_sign(second_dig_deq[i], other_dig)
        if len(str(plus_in_mind)) > 1:
            plus_in_mind = plus_in_mind[1]
            flag = 1

        res = deque(str(sign_plus_sign(first_dig_deq[i], plus_in_mind)))

        if len(res) > 1:
            res.reverse()
            for j in range(len(res)):
                if res[j] not in string_:
                    res_dig_deq.extendleft(res[j], )
                    if i != n - 1:
                        break
            other_dig = 1
        else:
            res_dig_deq.extendleft(res[0], )
            if flag == 1:
                flag = 0
                other_dig = 1
                if i == n - 1:
                    res_dig_deq.extendleft(str(1), )
            else:
                other_dig = 0
    print(f'{res_dig_deq}')


first_dig_deq = deque(input('Введите первое число: ').strip())
second_dig_deq = deque(input('Введите второе число: ').strip())


print(f'\nВы ввели:')
print(first_dig_deq)
print(second_dig_deq)

math_oper = input('\nВведите математическую операцию либо +, либо *:')

if math_oper == '+':
    print(f'\nРезультат: ')
    add_func(first_dig_deq, second_dig_deq, 0)

if math_oper == '*':
    res_dig_deq = deque()
    first_dig_deq.reverse()
    second_dig_deq.reverse()

    string_ = "( ) , ' "
    other_dig = 0

    res = deque(['0', ], )

    if len(first_dig_deq) < len(second_dig_deq):
        first_dig_deq, second_dig_deq = second_dig_deq, first_dig_deq

    str2 = ''

    for i in range(len(second_dig_deq)):
        res.clear()
        res = deque(['0', ])
        for j in range(len(first_dig_deq)):
            other, alter = mult_func(define_letter(first_dig_deq[j]), define_letter(second_dig_deq[i]))

            plus_ = sign_plus_sign(define_letter(alter), define_letter(res[0]))

            if len(str(plus_)) > 1:
                res.remove(res[0])
                res.extendleft(str(plus_[1]), )
                res.extendleft(str(sign_plus_sign(plus_[0], other)), )
                other_dig = 1
            else:
                res.remove(res[0])
                res.extendleft(str(plus_), )
                res.extendleft(str(other), )
                other_dig = 0

        str_ = ''
        for val in res:
            str_ = str_ + val

        str_ = str_ + str("0" * i)

        res1 = deque((str_).strip())
        res2 = deque((str2).strip())

        str2 = str_

    print(f'\nРезультат: ')
    add_func(res1, res2, 0)
