# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first_letter = input("Введите первую букву от a до z: ")
second_letter = input("Введите вторую букву от a до z: ")

f_l_place = ord(first_letter) - 96
s_l_place = ord(second_letter) - 96

print(f"Буква {first_letter} стоит на {f_l_place} месте")
print(f"Буква {second_letter} стоит на {s_l_place} месте")

print(f"Между ними {abs(f_l_place - s_l_place ) - 1} букв")
