# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
#  для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict

n = int(input('Введите колличество предприятий: '))
quarter = 4

inf_list = [(input('Введите название предприятия: '), [input('Введите прибыль предприятия: ') for _ in range(quarter)]) for _
            in range(n)]

mean_profit = 0

dict_enterpr = defaultdict(list)
for name_, val in inf_list:
    for profit_ in val:
        mean_profit += float(profit_)
        dict_enterpr[name_].append(profit_)
    dict_enterpr[name_].append(mean_profit)

mean_profit = mean_profit / n

print(f'\nСредняя прибыль предприятий за год: {mean_profit:.2f}')

for name_ in dict_enterpr:
    if dict_enterpr[name_][quarter] > mean_profit:
        print(f'Предприятие {name_} имеет прибыль выше среднего,\nприбыль: {dict_enterpr[name_][quarter]:.2f}')
    elif dict_enterpr[name_][quarter] == mean_profit:
        print(f'Предприятие {name_} имеет прибыль равную средней,\nприбыль: {dict_enterpr[name_][quarter]:.2f}')
    else:
        print(f'Предприятие {name_} имеет прибыль ниже среднего,\nприбыль: {dict_enterpr[name_][quarter]:.2f}')
