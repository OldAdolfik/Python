# line = '1, 2, 3, 4, 5'
# a_list = line.split(', ')

# print(*a_list)
# print(f'Min: {min(a_list)}')
# print(f'Max: {max(a_list)}')


# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# discr = b ** 2 - 4 * a * c
# print(f"Дискриминант D = {round(discr,2)}")

# if discr > 0:
#     x1 = (-b + (discr**0.5)) / (2 * a)
#     x2 = (-b - (discr**0.5)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

num_a = 45
num_b = 90
def f_nod(a, b):
    while a != b:
        if a > b:
            a = a - b, 
        else:
            b = b - a
    return a
print (f_nod(num_a, num_b))
print((num_a * num_b) // f_nod(num_a, num_b))
            