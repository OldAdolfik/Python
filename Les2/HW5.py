# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random

list = []

list1 = []

n = int(input('Введите размер списка: '))

i = 0

while i < n:
    num = random.randint(0, 35)
    list.append(num)
    i = i + 1

print(list)

j = 0

k = 1

while j < n:
    a = random.randint(0, n - k)
    list1.append(list[a])
    j = j + 1
    k = j + 1
    list.pop(a)

print(list1)