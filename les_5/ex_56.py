# 56. Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего.
# > Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def find_chain(numbers, chain, start_pos, find_length):
    global result
    if len(chain) == find_length:
        result += [chain[:]]
        chain.pop(-1)
        return
    for i in range(start_pos, len(numbers)):
        if len(chain) < find_length:
            if len(chain) > 0:
                if chain[len(chain) - 1] < numbers[i]:
                    chain.append(numbers[i])
                    find_chain(numbers, chain, i, find_length)
            else:
                chain.append(numbers[i])
                find_chain(numbers, chain, i, find_length)
    if len(chain) > 0: chain.pop(-1)


numbers = [1, 5, 2, 3, 4, 6, 1, 7]
chain = []
result = []
print(f'Заданный список: {numbers}')
for i in range(2, len(numbers)):
    find_chain(numbers, chain, 0, i)
print(f'Последовательности удовлетворяющие условию задачи: {result}')