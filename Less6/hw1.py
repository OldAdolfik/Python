# less 3 hw1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3 ,5 ,9 ,3]


# for i in range (len(lst)):
#     if i % 2 != 0:
#         sum = sum + lst[i]

# print(sum)


new_lst = [lst[x] for x in range(len(lst)) if x % 2 != 0]

sum = sum(new_lst)
print(sum)