# cnt = 0
# while cnt<5:
#     print('Hello')
#     cnt+=1
# for cnt in range(5):
#     print('Привет')

# задача 1

# print("Введите первое число: ")
# num1 = int(input())
# print("Введите второе число: ")
# num2 = int(input())
# if num2 == num1*num1:
#     print("Первое число является квадратом второго")
# elif num1 == num2*num2:
#     print('Второе число является квадратом первого')
# else: print("Ни одно из чисел не является квадратом другого")

# задача 2

# num1 = int(input("Введите число: "))
# num2 = -num1
# if num1>0:
#     for i in range(num2,num1+1):
#         print(i)
# elif num1<0:
#     for i in range(num1,num2+1):
#         print(i)
# else: print('Вы ввели число 0')0

# задача 3

num1 = float(input("Введите число: "))
if num1%1==0:
    print("нет")
else: 
    num1=int(num1%1*10)
    print (num1)