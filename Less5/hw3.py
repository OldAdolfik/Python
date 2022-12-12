lst = [1, 2 , 3 , 4, 5, 6, 7, 8, 9]
print('Сыграем в игру "Крестики-нолики"? - (да/нет)')
answer_user = input()
if answer_user == 'да' or answer_user == 'Да':
    print('Тогда начнём!')
    print('Как зовут первого игрока?')
    user_name1 = input()
    print('А как зовут второго игрока?')
    user_name2 = input()
    rules = ' Правила игры: играют 2 игрока. Игрок делает одно действие в свой ход.\n Вы выбираете цифру, а я вместо неё рисую ваш символ.\n Переход хода.\n Побеждает тот, кто быстрее соберет 3 своих символа в ряд!'
    print(rules)
    print(f'1  |  2  |  3\n4  |  5  |  6\n7  |  8  |  9')
    i = 0
    symb_user1 = 'X'
    symb_user2 = 'O'

    while i < 9:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            print(f'{user_name1} выберете цифру: ')
            choice_user1 = int(input())
            if choice_user1 > 0 and choice_user1 < 10:
                lst[choice_user1 - 1] = symb_user1
                print(f'{lst[0]}  |  {lst[1]}  |  {lst[2]}\n{lst[3]}  |  {lst[4]}  |  {lst[5]}\n{lst[6]}  |  {lst[7]}  |  {lst[8]}')
                i = i + 1
            else:
                print('Введите цифру от 1 до 9')
        elif i == 1 or i == 3 or i == 5 or i == 7:
            print(f'{user_name2} выберете цифру: ')
            choice_user2 = int(input())
            if choice_user2 > 0 and choice_user2 < 10:
                lst[choice_user2 - 1] = symb_user2
                print(f'{lst[0]}  |  {lst[1]}  |  {lst[2]}\n{lst[3]}  |  {lst[4]}  |  {lst[5]}\n{lst[6]}  |  {lst[7]}  |  {lst[8]}')
                i = i + 1
            else:
                print('Введите цифоу от 1 до 9')
                
    if lst[0] and lst[1] and lst[2] == symb_user1 or lst[1] and lst[4] and lst[7] == symb_user1 or lst[0] and lst[4] and lst[8] == symb_user1 or lst[2] and lst[4] and lst[6] == symb_user1 or lst[3] and lst[4] and lst[5] == symb_user1 or lst[6] and lst[7] and lst[8] == symb_user1 or lst[0] and lst[3] and lst[6] ==symb_user1 or lst[2] and lst[5] and lst[8] == symb_user1:
        print(f'Победил {user_name1}! Поздравляем!')
    elif lst[0] and lst[1] and lst[2] == symb_user2 or lst[1] and lst[4] and lst[7] == symb_user2 or lst[0] and lst[4] and lst[8] == symb_user2 or lst[2] and lst[4] and lst[6] == symb_user2 or lst[3] and lst[4] and lst[5] == symb_user2 or lst[6] and lst[7] and lst[8] == symb_user2 or lst[0] and lst[3] and lst[6] ==symb_user2 or lst[2] and lst[5] and lst[8] == symb_user2:
        print(f'Победил {user_name2}! Поздравляем!')
    else:
        print('Ничья. Попробуйте снова!')
elif answer_user == 'нет' or answer_user == 'Нет':
    print('Ничего, сыграем в следующий раз!')
else:
    print('Я Вас не понял. Повторите попытку (перезапустите программу)')