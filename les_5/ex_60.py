# 60. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

import os
import random

def find_move():
    return move

def print_field():
    global field
    os.system('cls')
    for index, value in enumerate(field, start=1):
        if value == 0: print(f'{index:3}', end = '')
        if value == 1: print('\033[34m  X\033[37m', end = '')
        if value == 2: print('\033[33m  O\033[37m', end = '')
        if index % 3 == 0: print('\n')

def check_result():
    global field
    global game_over
    who_win = 0
    if field[0] == field[1] == field[2]: who_win = field[0]
    if field[3] == field[4] == field[5]: who_win = field[3]
    if field[6] == field[7] == field[8]: who_win = field[6]
    if field[0] == field[3] == field[6]: who_win = field[0]
    if field[1] == field[4] == field[7]: who_win = field[1]
    if field[2] == field[5] == field[8]: who_win = field[2]
    if field[0] == field[4] == field[8]: who_win = field[0]
    if field[2] == field[4] == field[6]: who_win = field[2]
    if 0 not in field: who_win = 3

    if who_win > 0:
        game_over = True
    if who_win == 1:
        print('Вы проиграли! :(')
    if who_win == 2:
        print('Вы победили! :)')
    if who_win == 3:
        print('Ничья!')

def get_human_move():
    global field
    while True:
        os.system('cls')
        print_field()
        input_num = int(input('Сделайте ваш ход [1-9]: '))
        if 1 <= input_num <= 9 and field[input_num - 1] == 0:
            field[input_num - 1] = 2
            break
        else:
            input('Это недопустимый ход. Попробуйте снова! [ENTER]')

def get_pc_move():
    global field
    while True:
        random_num = random.randint(0, 8)
        if field[random_num] == 0:
            field[random_num] = 1
            break

def next_move():
    global human_turn
    if human_turn:
        get_human_move()
        print_field()
        human_turn = False
    else:
        get_pc_move()
        print_field()
        human_turn = True
    check_result()


field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
game_over = False
human_turn = bool(random.randint(0, 2))
os.system('cls')
input(f'Резудьтат жеребьевки. Вы ходите {2-int(human_turn)}-ым. [ENTER]')

while not game_over:
    next_move()