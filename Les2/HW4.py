# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


n = int(input('Введите N: '))

pos1 = int(input('Введите позицию 1: '))

pos2 = int(input('Введите позицию 2: '))

list = []

i = -n

while i < n+1:
    list.append(i)
    i = i + 1

print(list)

if 0 <= pos1 < n * 2 + 1 and 0 <= pos2 < n * 2 + 1:
    temp = list[pos1] * list[pos2]
    print(temp)
else: print('ББ')
