# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5


import random


def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list


n = int(input("Введите количество элементов в массиве: "))
m = random_int_list(n, min=1, max=100)
count2 = 0
if n >= 1:
    print(m)
else:
    print("Введено не натуральное число")
x = int(input("Введите любое число: "))
for i in range(len(m)):
    if m[i] == x:
        number = m[i]
    elif m[i] == x-1:
        number = m[i]
    elif m[i] == x-2:
        number = m[i]
    elif m[i] == x-3:
        number = m[i]
    elif m[i] == x+1:
        number = m[i]
    elif m[i] == x+2:
        number = m[i]
    elif m[i] == x+3:
        number = m[i]
print(f'Самый близкий по виличине элемент: {number}')
