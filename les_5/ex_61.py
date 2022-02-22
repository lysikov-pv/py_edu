# 61. Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# * Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

import re

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def try_int(float):
    st = str(float)
    a = re.sub(r'(\d+).0\b', r'\1', st)
    if a == st:
        return float
    else: 
        return int(a)

def calc(str):
    if not is_digit(str):  # Если это еще не число, то разбираем
        a = re.sub(r'(.+) ([+-]) (.+)', r'\1', str)  # Операции +- выполняем в конце
        s = re.sub(r'(.+) ([+-]) (.+)', r'\2', str)
        b = re.sub(r'(.+) ([+-]) (.+)', r'\3', str)
        if s == str:  # Если операций +- не найдено, то ищем /*
            a = re.sub(r'(.+) ([/*]) (.+)', r'\1', str)  # Операции /* выполняем в начале
            s = re.sub(r'(.+) ([/*]) (.+)', r'\2', str)
            b = re.sub(r'(.+) ([/*]) (.+)', r'\3', str)
        if   s == '/': return try_int(float(calc(a)) / float(calc(b)))
        elif s == '*': return try_int(float(calc(a)) * float(calc(b)))
        elif s == '+': return try_int(float(calc(a)) + float(calc(b)))
        elif s == '-': return try_int(float(calc(a)) - float(calc(b)))
    else:  # Если в функцию передали строку-число, то просто ее возвращаем
        return str

    
exp = '1.05 + 8 / 2 + 2 * 3'
print(f'{exp} = {calc(exp)}')