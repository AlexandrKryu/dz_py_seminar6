# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

argRnd1 = int(input('Введите начальное значение случайности: '))
argRnd2 = int(input('Введите конечное значение случайности: '))
argRnd3 = int(input('Количество случайностей: '))

floatList = [round(random.uniform(argRnd1, argRnd2), 2) for i in range(argRnd3)]
newlst = [round(i % 1, 2) for i in floatList if i % 1 != 0]
print(floatList)
print(newlst)
print(f'Разность Max и Min дробной части в списке {floatList} = {max(newlst) - min(newlst)}')