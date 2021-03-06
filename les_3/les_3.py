## Семинар 3
# 31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
# 32. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1
# 33. Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой
# 34. Подсчитать сумму цифр в вещественном числе
# 35. Написать программу получающую набор произведений чисел от 1 до N
# > Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
# 36. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
# 37. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# 38. Реализовать алгоритм перемешивания списка
# 39. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# 39. Определить, присутствует ли в заданном списке строк, некоторое число 

import os
import LehmerRnd  # генерация случайных чисел алгоритмом Лемера

random = LehmerRnd.LehmerRnd()  # Создаем объект т.к. для корректной генирации нужно хранить значение последнего seed

os.system('cls')
print('31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.')
print('32. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1')
print('33. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой')
print('34. Подсчитать сумму цифр в вещественном числе')
print('35. Написать программу получающую набор произведений чисел от 1 до N')
print('36. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму')
print('37. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число')
print('38. Реализовать алгоритм перемешивания списка')
print('39. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел')
print('40. Определить, присутствует ли в заданном списке строк, некоторое число')

input_num = int(input('Введите номер задачи для проверки: '))

if input_num == 31:  #  Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
    n = int(input('N = '))
    set = {(-3) ** i for i in range(0, n)}
    print(f'Первые N элементов множества: {set}')


elif input_num == 32:  #  Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1
    n = int(input('N = '))
    dic = {k: 3 * k + 1 for k in range(1, n + 1)}
    print(f'Первые N элементов множества: {dic}')


elif input_num == 33:  # Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой
    string = input('Строка: ')
    substring = input('Подстрока: ')
    # print(string.count(substring))  # Короткая запись, но не находит для перекрывающихся вхождений
    count = 0
    start_index = -1
    while True:
        start_index = string.find(substring, start_index + 1)  # Если нет вхождения то find возразает -1
        if start_index == -1:
            break
        count += 1
    print(f'Число вхождений: {count}')


elif input_num == 34:  # Подсчитать сумму цифр в вещественном числе
    n = input('N = ')
    temp_string = n.replace('-', '').replace('.', '')  # Удаляем - и . из строки
    print(f'Cумма цифр: {sum(int(i) for i in str(temp_string))}')


elif input_num == 35:  #  Написать программу получающую набор произведений чисел от 1 до N
    n = int(input('N = '))
    numbers = []
    last_number = 1
    for i in range(1, n + 1):
        last_number *= i
        numbers.append(last_number)
    print(f'Первые N элементов набора: {numbers}')


elif input_num == 36:  #  Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
    n = int(input('N = '))
    numbers = [(1 + 1 / i) ** i for i in range(1, n + 1)]
    print(f'Первые N элементов списка: {numbers}. Их сумма: {sum(numbers)}')


elif input_num == 37:  #  Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
    n = int(input('N = '))
    numbers = [random.Next(-n, n) for i in range(0, n)]
    print(f'Список из N элементов: {numbers}')

    with open('les_3/file.txt', 'r') as data:
        positions = [int(line) for line in data]
    print(f'Позиции из файла: {positions}')

    result = 1
    for i in positions:
        result *= numbers[i]
    print(f'Произведение элементов на указанных позициях: {result}')


elif input_num == 38:  #  Реализовать алгоритм перемешивания списка
    n = int(input('Введите длину списка. Список сгенерируется случайными числами [-100, 100]: '))
    numbers = [random.Next(-100, 100) for i in range(0, n)]
    print(f'Начальный список: {numbers}')
    max_index = len(numbers) - 1  # Нужно будет вызывать несколько раз, для уменьшения нагрузки
    for i in numbers:
        numbers.append(numbers.pop(random.Next(0, max_index)))
    print(f'Список после перемешивания: {numbers}')


elif input_num == 39:  #  Реализовать алгоритм перемешивания списка
    n = int(input('Введите количество случайных чисел: '))
    left_bound = int(input('Введите нижнюю границу: '))
    right_bound = int(input('Введите верхнюю границу: '))
    print(f'{n} случайных чисел в интервале [{left_bound}, {right_bound}]: {[random.Next(left_bound, right_bound) for i in range(0, n)]}')


elif input_num == 40:  #  Определить, присутствует ли в заданном списке строк, некоторое число
    string_list = ['Съешь еще', 'этих 12', 'мягких французских']
    print(f'Список строк: {string_list}')
    n = input('Введите число для проверки:  ')
    if sum([string.count(n) for string in string_list]) > 0:
        print(f'Число {n} содержится в списке строк')
    else:
        print(f'Число {n} не содержится в списке строк')