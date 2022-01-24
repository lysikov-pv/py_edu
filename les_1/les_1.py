import random
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
print('0. Вывести квадрат числа')
print('1. По двум введённым числам проверять является ли первое квадратом второго')
print('2. Даны два числа. Показать большее и меньшее число')
print('3. По введенному номеру дня недели вывести его название')
print('4. Найти максимальное из трех чисел')
print('5. Написать программу вычисления значения функции y=f(a)')
print('6. Выяснить является ли число чётным')
print('7. Показать числа от -N до N')
print('8. Показать четные числа от 1 до N')
print('9. Показать последнюю цифру трёхзначного числа')
print('10. Показать вторую цифру трёхзначного числа')
print('11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа')
print('12. Удалить вторую цифру трёхзначного числа')
print('13. Выяснить, кратно ли число заданному, если нет, вывести остаток')
print('14. Найти третью цифру числа или сообщить, что её нет')

input_num = int(input('Введите номер задачи для проверки: '))
if input_num == 0:  # Вывести квадрат числа
    a = int(input('A = '))
    print(f'{a} в квадрате это {a**2}')

elif input_num == 1:  # По двум введённым числам проверять является ли первое квадратом второго
    a = int(input('A = '))
    b = int(input('B = '))
    if   a == b * b: print(f'{a} является квадратом {b}')
    elif b == a * a: print(f'{b} является квадратом {a}')
    else:            print(f'{a} не является квадратом {b} и {b} не является квадратом {a}')

elif input_num == 2:  # Даны два числа. Показать большее и меньшее число
    a = int(input('A = '))
    b = int(input('B = '))
    if a != b: print(f'Большее {Max2(a, b)}, меньшее {Min2(a, b)}')
    else:      print(f'Числа равны')

elif input_num == 3:  # По введенному номеру дня недели вывести его название
    dayNum = int(input('Введите номер дня: '))
    if   dayNum == 1: print('Это понедельник')
    elif dayNum == 2: print('Это вторник')
    elif dayNum == 3: print('Это среда')
    elif dayNum == 4: print('Это четверг')
    elif dayNum == 5: print('Это пятница')
    elif dayNum == 6: print('Это суббота')
    elif dayNum == 7: print('Это воскресенье')
    else:             print('Нет такого дня недели')

elif input_num == 4:  # Найти максимальное из трех чисел
    a = int(input('A = '))
    b = int(input('B = '))
    c = int(input('C = '))
    print(f'Максимальное из трех: {Max3(a, b, c)}')

elif input_num == 5:  # Написать программу вычисления значения функции y=f(a)
    a = int(input('A = '))
    print(f'y=sqr({a})={Sqr(a)}')

elif input_num == 6:  # Выяснить является ли число чётным
    a = int(input('A = '))
    if a % 2 == 0: print('Четное')
    else:          print('Нечетное')

elif input_num == 7:  # Показать числа от -N до N
    n = int(input('N = '))
    print('Числа от -N до N: ')
    for i in range(n*-1, n + 1):
        print(i)

elif input_num == 8:  # Показать четные числа от 1 до N
    n = int(input('N = '))
    print('Четные числа от 1 до N: ')
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

elif input_num == 9:  # Показать последнюю цифру трёхзначного числа
    n = int(input('N = '))
    print(f'Последняя цифра: {n % 10}')

elif input_num == 10:  # Показать вторую цифру трёхзначного числа
    n = int(input('N = '))
    print(f'Вторая цифра: {round(n // 10 % 10, 1)}')

elif input_num == 11:  # Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
    n = random.randint(10, 99)
    print(f'N = {n}')
    print(f'{MaxInList(ParsIntToList(n))} является максимальной цифрой числа')

elif input_num == 12:  # Удалить вторую цифру трёхзначного числа
    n = random.randint(100, 999)
    print(f'N = {n}')
    list = ParsIntToList(n)
    n = list[0] * 10 + list[2]
    print(f'Число N без второй цифры: {n}')

elif input_num == 13:  # Выяснить, кратно ли число заданному, если нет, вывести остаток
    a = random.randint(0, 1000)
    print(f'A = {a}')
    b = int(input('B = '))
    if a % b == 0: print(f'{a} кратно {b}')
    else:          print(f'{a} не кратно {b}; остаток от делления {a % b}')

elif input_num == 14:  # Найти третью цифру числа или сообщить, что её нет
    n = int(input('N = '))
    numbers = ParsIntToList(n)
    if len(numbers) > 2: print(f'Третья цифра числа {numbers[2]}')
    else:                print(f'У числа нет третьей цифры')