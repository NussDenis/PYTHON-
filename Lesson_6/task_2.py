# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list


numbers = int(input("Введите количество чисел: "))
list_1 = random_int_list(numbers, min=-10, max=10)
print(list_1)
list_2 = []
range_numbers_min = int(input("Введите начало диапазона: "))
range_numbers_max= int(input("Введите конец диапазона: "))
for i in range(numbers):
    if (list_1[i] >= range_numbers_min) and ((list_1[i] <= range_numbers_max)):
        list_2.append(i)
print(f'Индексы элементов массива в заданном диапазоне: {list_2}')