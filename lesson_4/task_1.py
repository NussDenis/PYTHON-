# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

import random
def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


n = int(input("Введите количества чисел в первом наборе: "))
list_1 = random_int_list(n, min=-10, max=30)
print(list_1)
m = int(input("Введите количества чисел во втором набоер: "))
list_2 = random_int_list(m, min=-10, max=10)
print(list_2)
list_3 = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if (list_1[i] == list_2[j]):
            list_3.append(list_1[i])
list_3 = list(set(list_3))
print(f'Последовательность в порядке возрастания чисел в обоих наборах: {selection_sort(list_3)}')

