import random
import math
import os

def Max2(x, y):  # Возращает максимальное из двух
    if   x > y: return x
    elif x < y: return y

def Min2(x, y):  # Возращает минимальное из двух
    if   x < y: return x
    elif x > y: return y

def Max3(a, b, c):  # Возращает максимальное из трех
    if a > b:
        if a > c: return a
        else:     return c
    else:
        if b > c: return b
        else:     return c

def Sqr(a):  # Возращает квадрат числа
    return a * a

def ParsIntToList(a):  # Разбирает число на список
    numbers = []
    while a > 0:
        numbers.append(a % 10)
        a //= 10
    numbers.reverse()
    return numbers

def MaxInList(list):  # Возвращает максимальное число в списке
    max = list[0]
    for i in list:
        if i > max: max = i
    return max

os.system('cls')
print('15. Дано число. Проверить кратно ли оно 7 и 23')
print('16. Дано число обозначающее день недели. Выяснить является номер недели выходным днём')
print('17. По двум введённым числам проверять является ли одно квадратом другого')
print('18. Проверить истинность утверждения ¬(X ИЛИ Y) = ¬X И ¬Y')
print('19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X != 0 и Y != 0')
print('20. Ввести номер четверти, показать диапазоны для возможных координат')
print('21. Программа проверяет пятизначное число на палиндромом')
print('22. Найти расстояние между точками в пространстве 2D/3D')
print('23. Показать таблицу квадратов чисел от 1 до N')
print('24. Найти кубы чисел от 1 до N')
print('25. Найти сумму чисел от 1 до А')
print('26. Возведите число А в натуральную степень B используя цикл')
print('27. Определить количество цифр в числе')
print('28. Подсчитать сумму цифр в числе')
print('29. Написать программу вычисления произведения чисел от 1 до N')
print('30. Показать кубы чисел, заканчивающихся на четную цифру')

input_num = int(input('Введите номер задачи для проверки: '))
if input_num == 15:  #  Дано число. Проверить кратно ли оно 7 и 23
    a = int(input('A = '))
    if a % 7 == 0: print('Число кратно 7', end='')
    else:          print('Число не кратно 7', end='')
    if a % 23 == 0: print(' и кратно 23')
    else:           print(' и не кратно 23')

elif input_num == 16:  # Дано число обозначающее день недели. Выяснить является номер недели выходным днём
    day_num = int(input('Day number = '))
    if   day_num == 6 or day_num == 7:  print('Это выходной')
    elif day_num > 0 and day_num < 6:   print('Это будний день')        
    else:                               print('Такого дня недели нет')

elif input_num == 17:  # По двум введённым числам проверять является ли одно квадратом другого
    a = int(input('A = '))
    b = int(input('B = '))
    if   a == b * b: print(f'{a} является квадратом {b}')
    elif b == a * a: print(f'{b} является квадратом {a}')
    else:            print('Не одно из чисел не является квадратом другого')

elif input_num == 18:  # Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
    count = 0
    for x in False, True:
        for y in False, True:
            result = not (x or y) == (not x and not y)
            if not result: count += 1
            print(f'not ({x} or {y}) == (not {x} and not {y}) => Выражение: {result}')
    if count == 0: print('Итог: Для всех сочетаний X и Y выражение истинно')
    else:          print('Итог: Выражение ложно')

elif input_num == 19:  # Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
    x = int(input('X = '))
    y = int(input('Y = '))
    if   x > 0 and y > 0:   print('I четверть')
    elif x < 0 and y > 0:   print('II четверть')
    elif x < 0 and y < 0:   print('III четверть')
    elif x > 0 and y < 0:   print('IV четверть')
    elif x == 0 and y == 0: print('Начало координат')
    else:                   print('Как ты это сделал?')

elif input_num == 20:  # Ввести номер четверти, показать диапазоны для возможных координат
    n = int(input('Введите номер четверти: '))
    if n == 1:   print('x > 0, y > 0')
    elif n == 2: print('x < 0, y > 0')
    elif n == 3: print('x < 0, y < 0')
    elif n == 4: print('x > 0, y < 0')
    else:        print('Такой четверти нет')

elif input_num == 21:  # Программа проверяет число на палиндромом (размер ввода ограничен типом int)
    a = int(input('A = '))
    digits_list = list(str(a))
    reversed_digit_list = list(reversed(digits_list))
    if digits_list == reversed_digit_list: print('Число палиндром')
    else:                                  print('Число не палиндром')

elif input_num == 22:  # Найти расстояние между точками в пространстве 2D/3D
    n = int(input('Введите кол-во измерений (2=2D, 3=3D): '))
    if n == 2:
        x1 = random.randint(-100, 100)
        y1 = random.randint(-100, 100)
        x2 = random.randint(-100, 100)
        y2 = random.randint(-100, 100)
        print(f'Расстояние между точками ({x1},{y1}) и ({x2},{y2}) равно {math.sqrt((x2 - x1)**2 + (y2 - y1)**2)}')
    elif n == 3:
        x1 = random.randint(-100, 100)
        y1 = random.randint(-100, 100)
        z1 = random.randint(-100, 100)
        x2 = random.randint(-100, 100)
        y2 = random.randint(-100, 100)
        z2 = random.randint(-100, 100)
        print(f'Расстояние между точками ({x1},{y1},{z1}) и ({x2},{y2},{z2}) равно {math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)}')
    else: print('Программа не может посчитать для стольки измерений')

elif input_num == 23:  #  Показать таблицу квадратов чисел от 1 до N
    n = int(input('N = '))
    for i in range(1, n + 1):
        print(f'{i} x {i} = {i ** 2}')

elif input_num == 24:  #  Найти кубы чисел от 1 до N
    n = int(input('N = '))
    for i in range(1, n + 1):
        print(f'{i} x {i} x {i} = {i ** 3}')

elif input_num == 25:  #  Найти сумму чисел от 1 до А
    a = int(input('A = '))
    print(f'Сумма чисел от 1 до {a} равна: {sum(i for i in range(1, a + 1))}')

elif input_num == 26:  #  Возведите число А в натуральную степень B используя цикл
    a = int(input('A = '))
    b = int(input('B = '))
    result = 1
    for i in range(b):
        result *= a
    print(f'{a} в степени {b}: {result}')

elif input_num == 27:  #  Определить количество цифр в числе
    a = int(input('A = '))
    print(f'Количество цифр в числе: {len(str(abs(a)))}')

elif input_num == 28:  #  Подсчитать сумму цифр в числе
    a = int(input('A = '))
    print(f'Cумма цифр: {sum(int(i) for i in str(a))}')

elif input_num == 29:  #  Написать программу вычисления произведения чисел от 1 до N
    n = int(input('N = '))
    print(f'Произведение чисел от 1 до {n} равно: {math.prod(i for i in range(1, n + 1))}')

elif input_num == 30:  #  Показать кубы чисел, заканчивающихся на четную цифру
    n = int(input('Сколько кубов показать: '))
    count = 0
    i = 2
    while count < n:
        count += 1
        print(f'{count}. {i ** 3}')
        i += 2  # Куб четного всегда будет четным