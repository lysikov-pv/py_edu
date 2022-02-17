# 54. Даны два файла в каждом из которых находится запись многочлена. Сформировать
# файл содержащий сумму многочленов.

# list(filter(lambda a: a != '' and a != None, input_list)) - убрать из списка строк все элеиенты '' и None

import re
from functools import reduce

def polynom_str_completion(polynom_str):  # Дополнение строки
    result = polynom_str[: -3]
    result = re.sub(r'\bx\^(\d+) ', r'1x^\1 ', result)  # 'x^k ' -> '1x^k'
    result = re.sub(r'\b(\d+)x ', r'\1x^1 ', result)    # 'nx '  -> 'nx^1'
    result = re.sub(r' (\d+) ', r' \1x^0 ', result)     # ' n '  -> ' nx^0 '
    return result

def polynom_str_to_strlist(complete_polynom_str):  # Строку разбиваем на список составных строк
    polynom_str = complete_polynom_str
    polynom_str = re.sub(r' \+ ', r' ;', polynom_str)   # ' + '   -> ';'
    polynom_str = re.sub(r' \- ', r' ;-', polynom_str)  # ' - '   -> ';-'
    return re.split(r';', polynom_str)

def polynom_str_to_list(polynom_str):  # Переводим строку многочлена в список где номер позиции это степень а значение в позиции это коэффициент
    polynom_str = polynom_str_completion(polynom_str)
    polynom_strlist = polynom_str_to_strlist(polynom_str)

    max_k = int(re.sub(r'([+-]?\d+)x\^(\d+) ', r'\2', polynom_strlist[0]))
    polynom_list = [0 for i in range(0, max_k + 1)]

    for str in polynom_strlist:
        n = re.sub(r'([+-]?\d+)x\^(\d+) ', r'\1', str)
        k = re.sub(r'([+-]?\d+)x\^(\d+) ', r'\2', str)
        polynom_list[int(k)] = int(n)
    return polynom_list

def normalize_polynom(polynom_str):  # Наложение общепринятых сокращений после перевода из списка в строку
    polynom_str = re.sub(r' 0x\^(\d+) ;', r'', polynom_str)      # ' 0x^k ;' -> ''
    polynom_str = re.sub(r' 1x\^(\d+)', r' x^\1', polynom_str)   # ' 1x^k' -> ' x^k'
    polynom_str = re.sub(r'-1x\^(\d+)', r'-x^\1', polynom_str)   # '-1x^k' -> '-x^k'
    polynom_str = re.sub(r'(\d+)x\^1 ', r'\1x ', polynom_str)    # 'nx^1 ' -> 'nx ' 
    polynom_str = re.sub(r'(\d+)x\^0 ', r'\1 ', polynom_str)     # 'nx^0 ' -> 'n ' 
    polynom_str = re.sub(r' ; -', r' - ', polynom_str)           # ' ; -' -> ' - ' 
    polynom_str = re.sub(r' ; ',  r' + ', polynom_str)           # ' ; ' -> ' + ' 
    polynom_str = re.sub(r' ;',  r' = 0', polynom_str)           # ' ;'  -> ' =0'
    if polynom_str == '': polynom_str = ' 0 = 0'
    return polynom_str

def polynom_list_to_str(polynom_list):  # Переводим список в строку
    polynom_liststr = []
    for i in range(len(polynom_list) - 1, -1, -1):
        polynom_liststr.append(' ' + str(polynom_list[i]) + 'x^' + str(i) + ' ;')
    polynom_str = reduce(lambda x, y:  x + y, polynom_liststr)
    polynom_str = normalize_polynom(polynom_str)
    return polynom_str[1:]

def add_length(polynom_list, len):  # Увеличиваем размер списка полинома до нужной длины
    for i in range(0, len):
        polynom_list.append(0)
    return polynom_list

def sum_polynom(polynom1, polynom2):  # Складываем полиномы записанные в списках поэлементно
    polynom1_len = len(polynom1)
    polynom2_len = len(polynom2)
    if   polynom1_len > polynom2_len: polynom2 = add_length(polynom2, polynom1_len - polynom2_len)
    elif polynom2_len > polynom1_len: polynom1 = add_length(polynom1, polynom2_len - polynom1_len)
    return [polynom1[i] + polynom2[i] for i in range(0, polynom1_len)]


# Условия задачи
with open('les_5/ex_54_in1.txt', 'r') as data:
    polynom_str1 = data.read()
with open('les_5/ex_54_in2.txt', 'r') as data:
    polynom_str2 = data.read()
polynom1 = polynom_str_to_list(polynom_str1)
polynom2 = polynom_str_to_list(polynom_str2)
result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
with open('les_5/ex_54_out.txt', 'w') as data:
    data.write(result)

# Тест 1
polynom_str1 = '8x^7 + 68x^6 + 21x^3 + 56x^2 + 89x + 45 = 0'
polynom_str2 = '-8x^7 - 38x^5 + 47x - 90 = 0'
expected_result = '68x^6 - 38x^5 + 21x^3 + 56x^2 + 136x - 45 = 0'
polynom1 = polynom_str_to_list(polynom_str1)
polynom2 = polynom_str_to_list(polynom_str2)
actual_result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
print('\nТест 1')
print(f'Входной полином 1: {polynom_str1}')
print(f'Входной полином 2: {polynom_str2}')
print(f'Сумма: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
polynom_str1 = '8x^7 + 68x^6 + 21 = 0'
polynom_str2 = '-8x^7 - 68x^6 - 21 = 0'
expected_result = '0 = 0'
polynom1 = polynom_str_to_list(polynom_str1)
polynom2 = polynom_str_to_list(polynom_str2)
actual_result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
print('\nТест 2')
print(f'Входной полином 1: {polynom_str1}')
print(f'Входной полином 2: {polynom_str2}')
print(f'Сумма: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
polynom_str1 = '8x^7 + 68x^6 + 21 = 0'
polynom_str2 = '-8x^7 - 69x^6 - 21 = 0'
expected_result = '-x^6 = 0'
polynom1 = polynom_str_to_list(polynom_str1)
polynom2 = polynom_str_to_list(polynom_str2)
actual_result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
print('\nТест 3')
print(f'Входной полином 1: {polynom_str1}')
print(f'Входной полином 2: {polynom_str2}')
print(f'Сумма: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
polynom_str1 = '-8x^7 - 23x^6 - 54x^3 - 21 = 0'
polynom_str2 = '-8x^7 - 23x^6 - 54x^3 - 21 = 0'
expected_result = '-16x^7 - 46x^6 - 108x^3 - 42 = 0'
polynom1 = polynom_str_to_list(polynom_str1)
polynom2 = polynom_str_to_list(polynom_str2)
actual_result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
print('\nТест 3')
print(f'Входной полином 1: {polynom_str1}')
print(f'Входной полином 2: {polynom_str2}')
print(f'Сумма: {actual_result}. Результат верен: {actual_result == expected_result}')