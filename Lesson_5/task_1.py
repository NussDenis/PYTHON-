# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def degree(s, k):
    if s == 0:
        return 1
    elif s == 1:
        return k
    else:
        return (k * degree(s-1, k))


n = int(input("Введите число: "))
m = int(input("Введите степень: "))
print(f'{n} в степени {m} = {degree(m,n)}')
