# lst = [(1, 8), (4, 2), (6,1)]




# print(max(lst, key=lambda x: x[1]))

# lst = [2, 33, 12, 34, 3, 13]
# # a = filter(lambda x: x % 2 == 0, lst)
# # print(*a)
# for index, x in enumerate(lst):
#     print(index, x)

# lst = []

# for x in range(-2, 7):
#     if x % 2 == 0:
#         lst.append(x * x)
#     else:
#         lst.append(x * x * x)

# print(lst)

# lst1 = [x * x if x % 2 == 0 else x * x * x for x in range(-2, 7)]

# print(lst1)


# last = None
# with open('text.txt') as f:
#     for item in map(int, f.read().split( )):
#         if last is None:
#             last = item
#         else:
#             if item != last + 1:
#                 print(last + 1)
#             last = item


# a = "привет абв пока абвг"
# res = ' '.join(list(filter(lambda x: not 'абв' in x, a.split())))
# print(res)


lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = []
i = 0
j = 0
k = 0
for i, item in enumerate(lst):
    res.append([item])
    print(res)
    for item in lst:
        if item > res[j][k]:
            res[j].append(item)
            k += 1
    j += 1
    k = 0
print(res)

lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = []
i = 0
k = 0
for j, item in enumerate(lst):
    res.append([item])
    print(res)
    for i in range(j, len(lst)):
        if lst[i] > res[j][k]:
            res[j].append(lst[i])
    k = 0
print(res)