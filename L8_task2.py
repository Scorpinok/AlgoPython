# 2 Закодируйте любую строку по алгоритму Хаффмана.

def almost_haffman(string_in):
    string_ = {}
    n = len(string_in)

    for i in range(n):
        el = string_in[i]
        if el != '':
            string_[el] = string_in.count(el)

    string_to_list_ = list(string_.items())
    string_to_list_.sort(key=lambda i: i[1], reverse=True)

    return string_to_list_


def make_me_binary(n):
    return bin(n).replace("0b", "")


string_ = input("Введите строку для кодирования: ")
# string_ = 'sova'

bin_dict = {}
key_ = [i[0] for i in almost_haffman(string_)]
n = len(key_)

for i in range(n):
    bin_dict[key_[i]] = make_me_binary(i)

print(f'\nCтрока для кодирования:\n{string_}\n')
res_num = ''.join([bin_dict[i] for i in string_])
print(f'Закодированная строка:\n{res_num}')
