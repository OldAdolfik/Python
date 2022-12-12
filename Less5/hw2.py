# 28 * 70 = 1960, 2021 - 1960 = 61, 61 - 28 = 33.

from random import randint

print('Сыграем в игру "конфеты"? - (да/нет)')
answer_user = input()
if answer_user == "да" or answer_user == "Да":
    print('Погнали!')
    name_user1 = input('Как зовут первого игрока?\n')
    name_user2 = input('Как зовут второго игрока?\n')
    print('Правила игры: На столе лежит 2021 конфета.\n Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.\n Побеждает тот, кто успел собрать больше!')
    sweets_on_the_table = 2021
    count_user1 = 0
    count_user2 = 0
    sortition = randint(0,1)
    while sweets_on_the_table > 28:
        if sortition == 0:
            print(f'Ходит игрок {name_user1}. Сколько конфет Вы хотите взять сейчас?')
            choice_user1 = int(input())
            if choice_user1 >= 0 and choice_user1 <= 28:
                sweets_on_the_table = sweets_on_the_table - choice_user1
                count_user1 = count_user1 + choice_user1
                sortition == 1
                print(f'Количество конфет на столе: {sweets_on_the_table}.\n Количество конфет у первого игрока ({name_user1}): {count_user1}.\n Переход хода.')
            elif choice_user1 < 0 or choice_user1 > 28:
                print('Вы нарушили правила. В наказание Вы ничего не получаете, и ход переходит следующему игроку.')
                sortition == 1
        elif sortition == 1:
            print(f'Ходит игрок {name_user2}. Сколько конфет Вы хотите взять?')
            choice_user2 = int(input())
            if choice_user2 >= 0 and choice_user2 <= 28:
                sweets_on_the_table = sweets_on_the_table - choice_user2
                count_user2 = count_user2 + choice_user2
                sortition == 0
                print(f'Количество конфет на столе: {sweets_on_the_table}.\n Количество конфет у второго игрока ({name_user2}): {count_user2}.\n Переход хода.')
            elif choice_user2 < 0 or choice_user2 > 28:
                print('Вы нарушили правила. В наказание Вы ничего не получаете, и ход переходит следующему игроку.')
                sortition == 0
    if sortition == 0:
        count_user1 = count_user1 + sweets_on_the_table
        print(f'Победитель - {name_user1}. У этого игрока аж {count_user1} конфет(ы)!\n У второго игрока {count_user2} конфет(ы).\n Поздравляем победителя, а проигравшему желаем удачи в следующий раз!')
    elif sortition == 1:
        count_user2 = count_user2 + sweets_on_the_table
        print(f'Победитель - {name_user2}. У этого игрока аж {count_user2} конфет(ы)!\n У первого игрока {count_user1} конфет(ы).\n Поздравляем победителя, а проигравшему желаем удачи в следующий раз!')
elif answer_user == 'нет' or answer_user == 'Нет':
    print('Сыграем в следующий раз!')
else: 
    print('Извините, но я Вас не понял. Повторите попытку (перезапустите программу)')
    

