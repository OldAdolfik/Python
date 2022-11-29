# print('Введите число: ')

# n=int(input ())

# for i in range(n):
#     print((-3) ** i, end= ' ')


# Для натурального n создать список, состоящий из элементов последовательности 3n+1


# N = int(input('N = '))
# lst1 = []
# for i in range(N + 1):
#     lst1.append(3 * i + 1)
# print(lst1)


str1 = input()
str2 = input()
count = 0

for i in range(len(str1) - (len(str2) - 1)):
    if str2 == str1[i:i+len(str2)]:
        count += 1


print(f"Вторая строка входит в первую {count} раз(а).")
