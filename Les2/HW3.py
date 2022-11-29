# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

list = []

n = int(input('Введите число: '))

for i in range(1, n + 1):
    temp = (1 + 1 / i) ** i
    list.append(temp)

print(list)

sum = 0

for i in range(n):
    sum = list[i]+sum

print(sum)