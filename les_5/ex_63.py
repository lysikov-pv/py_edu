# 63. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def unicue(list):
    keys = set(numbers)
    freq_dic = {key:0 for key in keys} # freq_dic = dict.fromkeys(keys, 0)
    for key in list:
        freq_dic[key] += 1
    result = [key for key in keys if freq_dic[key] == 1]
    return result

numbers = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'Начальная последовательность: {numbers}')
print(f'Не повторяющиеся элементы: {unicue(numbers)}')