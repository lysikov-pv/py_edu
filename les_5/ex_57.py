# Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих
# условию предыдущей задачи. > Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]

# def find_chain(list, chain, start_pos, find_length, exit):
#     if find_length == len(chain):
#         print(chain)
#         exit = True
#         return
#     for i in range(start_pos, len(list)):
#         if exit: break
#         if find_length > len(chain):
#             if len(chain) > 0:
#                 if chain[len(chain) - 1] < list[i]:
#                     chain.append(list[i])
#                     find_chain(list, chain, i, find_length, exit)
#             else:
#                 chain.append(list[i])
#                 find_chain(list, chain, i, find_length, exit)
#     if len(chain) > 0: chain.pop(-1)

def find_chain(numbers, chain, start_pos, find_length):
    global result
    global exit
    if len(chain) == find_length:
        result = chain[:]
        exit = True
        return
    for i in range(start_pos, len(numbers)):
        if exit: break
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
exit = False
print(f'Заданный список: {numbers}')
for i in range(len(numbers), 1, -1):
    if exit: break
    find_chain(numbers, chain, 0, i)
print(f'Последовательности удовлетворяющие условию задачи: {result}')