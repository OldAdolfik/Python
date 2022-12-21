# our_list = ['22', '33', '123', 'fwefe', 'ytyy', 22]

# u = 'ytyy'
#  print(u)

#  count = 0

#  print(our_list)

#  for i in range (len(our_list)):
#      if our_list[i] == u:
#          count +=1
#          if count == 2:
#              break
#  print('В списке присутствует искомое значение. На позиции \n{i}') 

our_list = ['22', '33', '123', 'fwefe', 'ytyy', 22]

u = 'ytyy'

for i in enumerate(our_list):
    if i[1] == u:
        print(i)