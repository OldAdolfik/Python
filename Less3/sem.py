# from time import time


# def random_num_generate():

#     random_number = (time() * 1000 % 1000)
#     return int(random_number)


# restart = ''


# while restart == '':
#     random_number = random_num_generate()
#     print (random_number)
#     restart = input('рестарт?')


our_list = ['22', '33', '123', 'fwefe', 'ytyy', 22]

u = 'ytyy'
print(u)

count = 0

print(our_list)

for i in range (len(our_list)):
    if our_list[i] == u:
        count +=1
        if count == 2:
            break
print('В списке присутствует искомое значение. На позиции \n{i}') 