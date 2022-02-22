# 60. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру
# для игры человек против человека
# * Добавьте игру против бота
# * Подумайте как наделить бота "интеллектом"

# На столе лежат 2021 конфет
# Играет два игрока. Первый ход определяется жеребьевкой. За один ход можно забрать не более
# 28 конфет. Выйгрывает и забирает все сделавший последний ход.

import os
import random

def print_remainder():
    global number
    os.system('cls')
    print(f'На столе конфет: \033[33m{number}\033[37m')

def check_result():
    global number
    global game_over
    global human_turn
    if number == 0:
        if human_turn:
            print('Вы проиграли! :(')
        else:
            print('Вы победили! :)')
        game_over = True

def get_human_move():
    global number
    while True:
        input_num = int(input('Сделайте ваш ход [1-28]: '))
        if 1 <= input_num <= 28 and input_num <= number:
            number -= input_num
            break
        else:
            input('Это недопустимый ход. Попробуйте снова! [ENTER] ')

def get_pc_move():
    global number
    while True:
        random_num = random.randint(1, 28)
        if random_num <= number:
            number -= random_num
            input(f'Компьютер забрал: \033[33m{random_num}\033[37m [ENTER] ')
            break

def next_move():
    global human_turn
    if human_turn:
        os.system('cls')
        print_remainder()
        get_human_move()
        human_turn = False
    else:
        os.system('cls')
        print_remainder()
        get_pc_move()
        human_turn = True
    check_result()


number = 121
game_over = False
human_turn = bool(random.randint(0, 2))
os.system('cls')
input(f'Резудьтат жеребьевки. Вы ходите \033[33m{2-int(human_turn)}\033[37m-ым. [ENTER] ')

while not game_over:
    next_move()