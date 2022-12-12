# count = 1
# cod = ''

# with open ('less5_hw4.txt', 'r'):
#     for i in range(len('less5_hw4.txt')-1):
#         if 'less5_hw4.txt'[i] == 'less5_hw4.txt'[i+1]:
#             count += 1
#         else:
#             cod = cod + str(count) + 'less5_hw4.txt'[i]
#             count = 1
#     if count > 1 or ('less5_hw4.txt'[len('less5_hw4.txt')-2] != 'less5_hw4.txt'[-1]):
#         cod = cod + str(count) + 'less5_hw4.txt'[-1]

# number = ''
# decod = ''

# with open ('less5_hw4.txt', 'r'):
#     for i in range(len('less5_hw4.txt')):
#         if not 'less5_hw4.txt'[i].isalpha():
#             number += 'less5_hw4.txt'[i]
#         else:
#             decod = decod + 'less5_hw4.txt'[i] * int(number)
#             number = ''

# print(f"Текст после кодировки: {cod}")
# print(f"Текст после дешифровки: {decod}")
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")