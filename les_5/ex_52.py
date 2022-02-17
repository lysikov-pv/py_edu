# 52. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# > Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

import time
import random

def unique_elements(list):
    result_list = []
    for number in list:
        if number not in result_list:
            result_list.append(number)
    return result_list

def unique_elements_by_set(list):
    return [number for number in set(list)]


# Тест 1
tst_list = [1, 2, 3, 5, 1, 5, 3, 10]
expected_result = [1, 2, 3, 5, 10]
actual_result = unique_elements(tst_list)
print('\nТест 1')
print(f'Входной список: {tst_list}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
tst_list = [1, -2, 1, -2, 0, 0]
expected_result = [1, -2, 0]
actual_result = unique_elements(tst_list)
print('\nТест 2')
print(f'Входной список: {tst_list}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3 (производительности)
print('\nТест 3 (производительности)')
for i in range(0, 3):
    n = 10000 * 10**i
    print(f'Количество элементов: {n}')
    tst_list = [random.randint(0, 100) for i in range(0, n)]
    start_time = time.time()
    actual_result = unique_elements(tst_list)
    end_time = time.time()
    print(f'Время выполнения метод unique_elements элементов: {end_time - start_time}с')
    start_time = time.time()
    actual_result = unique_elements_by_set(tst_list)
    end_time = time.time()
    print(f'Время выполнения метод unique_elements_by_set для элементов: {end_time - start_time}с\n')
