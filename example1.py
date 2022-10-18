# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

argRnd1 = int(input('Введите начальное значение случайности: '))
argRnd2 = int(input('Введите конечное значение случайности: '))
argRnd3 = int(input('Количество случайностей: '))

newlist = [random.randint(argRnd1, argRnd2) for i in range(argRnd3)]
sum_odd = sum(newlist[item] for item in range(1, len(newlist), 2))
# sum = 0
# for i in range(len(newlist)):
#     if i % 2 != 0:
#         sum += newlist[i]
print(f'{newlist} Сумма на нечетных индексах  = {sum_odd}')