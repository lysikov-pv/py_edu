# 55. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найти его.

numbers = []
with open('les_5/ex_55_in.txt', 'r') as data:
    for line in data:
        numbers = [int(number) for number in line.split(' ')]
result = [numbers[i]-1 for i in range(0, len(numbers)) if numbers[i]-1 != numbers[i-1] and i>0]

print(f'Выпавшие из последовательности {numbers} элементы: {result}')