N = 903

i = 0
while N % 2 == 0:
    N = N / 2
    i = i + 1

j = 0
while N % 3 == 0:
    N = N / 3
    j = j + 1

k = 0
while N % 5 == 0:
    N = N / 5
    k = k + 1

u = 0
while N % 7 == 0:
    N = N / 7
    u = u + 1

y = 0
while N % 11 == 0:
    N = N / 11
    y = y + 1

z = 0
while N % 13 == 0:
    N = N / 13
    z = z + 1

q = 0
while N % 17 == 0:
    N = N / 17
    q = q + 1

w = 0
while N % 19 == 0:
    N = N / 19
    w = w + 1

lst = []

while i != 0:
    if i > 0:
        lst.append(2)
        i = i - 1

while j != 0:
    if j > 0:
        lst.append(3)
        j = j - 1

while k != 0:
    if k > 0:
        lst.append(5)
        k = k - 1

while u != 0:
    if u > 0:
        lst.append(7)
        u = u - 1

while y != 0:
    if y > 0:
        lst.append(11)
        y = y - 1

while z != 0:
    if z > 0:
        lst.append(13)
        z = z - 1

while q != 0:
    if q > 0:
        lst.append(17)
        q = q - 1

while w != 0:
    if w > 0:
        lst.append(19)
        w = w - 1

lst.append(N)
print(lst)