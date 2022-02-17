# 53. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from functools import reduce
import re

def get_polynom(degree):
    polynom_str = ''
    for n in range(degree, 0, -1):
        a = random.randint(0, 100)
        if a != 0:
            if   n == degree and n != 1:
                polynom_str += str(a) + 'x^' + str(n)
            elif n == degree and n == 1:
                polynom_str += str(a) + 'x'
            elif n == 1:
                polynom_str += ' + ' + str(a) + 'x'
            else:
                polynom_str += ' + ' + str(a) + 'x^' + str(n)
    return polynom_str + ' = 0'

def normalize_polynom(polynom_str):  # Общепринятые сокращения
    polynom_str = re.sub(r'\b0x\^\d+ \+ ', r'', polynom_str)     # '0x^k' -> ''
    polynom_str = re.sub(r'\b1x\^(\d+)', r'x\^\1', polynom_str)  # '1x^k' -> 'x^k'
    polynom_str = re.sub(r'(\d+)x\^1', r'\1x', polynom_str)      # 'nx^1' -> 'nx' 
    polynom_str = re.sub(r'(\d+)x\^0', r'\1', polynom_str)       # 'nx^0' -> 'n' 
    return polynom_str

def get_polynom_x(degree):  # Идея Владимира Сидоренко
    polynom_list = [str(random.randint(0, 100)) + 'x^' +  str(n) + ' + ' for n in range(degree, -1, -1)]
    polynom_str = reduce(lambda x, y:  x + y, polynom_list)
    polynom_str = normalize_polynom(polynom_str)
    return polynom_str[: -3] + ' = 0'


# Тест
k = random.randint(1, 10)
polynom = get_polynom_x(k)
print(f'Полином степени {k}: {polynom}')
with open('les_5/ex_53_out.txt', 'a') as data:
    data.write(polynom+'\n')