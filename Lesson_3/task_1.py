# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

import random


def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list


n = int(input("Введите количество элементов в массиве: "))
m = random_int_list(n, min=1, max=15)
count1 = 0
count2 = 0
if n >= 1:
    print(m)
else:
    print("Введено не натуральное число")
x = int(input("Введите любое число из массива: "))
for i in range(len(m)):
    if m[i] == x:
        count1 += 1
    else:
        count2 += 1
if count2 == n:
    print("Число отсутствует в массиве")
else:
    print(f'Введенное число {x} повторяется в массиве {count1} раз(а)')