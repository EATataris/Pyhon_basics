# #1
# a = 1
# b = 'abc'
# print(a, b)
# x = input('Введи переменную:')
# print(x)

# #2
# time = int(input('введите время в секундах:'))
# hour = time // 3600
# minutes = (time % 3600) // 60
# seconds = (time % 3600) - minutes * 60
# print(f'{hour}:{minutes}:{seconds}')

# #3
# n = input('введите число n:')
# sum = int(n) + int(n * 2) + int(n * 3)
# print(sum)

# #4
# some_num = int(input('введите положительное число:'))
# max_num = some_num % 10
# while some_num > 0:
#     if some_num % 10 > max_num:
#         max_num = some_num % 10
#     some_num = some_num // 10
# print(max_num)

# #5
# revenue = float(input('Выручка фирмы: '))
# costs = float(input('Издержки: '))
#
# if revenue > costs:
#     print('Фирма рентабельна')
#     profitability = revenue / (revenue - costs)
#     print(f'Рентаьельность выручки {profitability} $')
#     workers = int(input('Кол-во сотрудников: '))
#     print(f'Прибыль фирмы в расчете на однго сотрудника {(revenue - costs) / workers} $')
# else:
#     print('Крах')

#6
a = int(input('Пробежал км в 1 день: '))
b = int(input('Итоговый результат: '))

i = 0
print(a)
while a <= b:
    a += a * 0.1
    print(a)
    i += 1

print(i+1)