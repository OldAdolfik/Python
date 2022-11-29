# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math


num1 = int(input('Введите число: '))


def temp(a):
    if a == 1:
        return a
    else:
        return a * temp(a-1)


list = []

for i in range(1, num1 + 1):
    list.append(temp(i))

print(list)
