# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num1=int(input('Введите день недели: '))
if num1==6 or num1==7:
    print('Выходной')
elif num1==1:
    print('Будни, но у меня выходной :)')
elif num1==2 or num1==3 or num1==4 or num1==5:
    print('Будни')
else: print('Такого дня нет')