# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


lst = [2, 3, 5, 6]


# for i in range(len(lst)):
#     if len(lst):
#         print(lst[i] * lst[len(lst) - 1 - i])


flo_len_lst = int(float(len(lst)) / 2 + 0.5)

new_lst = [lst[x] * lst[len(lst) - 1 - x] for x in range(flo_len_lst) if len(lst)]

print(new_lst)
