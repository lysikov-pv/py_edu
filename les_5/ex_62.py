# 62. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах

import re
import os

def find_repeat(pos, data):
    length = 1
    while pos + 1 < len(data):
        if data[pos] == data[pos+1] and length >= 1:
            length += 1
            pos += 1
        elif data[pos] != data[pos+1] and length <= 1:
            if length == 1: length = 0
            length -= 1
            pos += 1
            if pos == len(data) - 1: length -= 1
        else: break
    return length

def rle_zip(data):
    # global data
    pos = 0
    while pos < len(data):
        length = find_repeat(pos, data)
        if length >= 1:
            data = data[:pos] + str(length) + data[pos] + data[pos + length:]
            pos += len(str(length)) + 1
        elif length < 1:
            data = data[:pos] + str(length) + data[pos:]
            pos += -length + len(str(length))
    return data

def rle_unzip(data):
    # global data
    pos = 0
    while pos < len(data):
        if data[pos] == "-":
            substr = data[pos:pos+4]
            length = re.sub(r'\-(\d+)\D*\d*', r'\1', substr)
            data = data[:pos] + data[pos+len(length)+1:]
            pos += int(length)
        else:
            substr = data[pos:pos+3]
            length = re.sub(r'(\d+)\D*\d*', r'\1', substr)
            data = data[:pos] + data[pos+len(length)]*int(length) + data[pos+len(length)+1:]
            pos += int(length)
    return data        


# tozip_text = 'faghhhgfkkkllllllgcccrf'
input_file = open('les_5/ex_62_in.txt', 'r')
tozip_text = input_file.read()
input_file.close()

zip_text = rle_zip(tozip_text)

os.system('cls')
print(f'Входной текст: {tozip_text}\n')
print(f'Сжатый текст: {zip_text}\n')
print(f'Степень сжатия: {(len(tozip_text)/len(zip_text)):.3f}\n')

output_file = open('les_5/ex_62_out.txt', 'w')
output_file.write(zip_text)
output_file.close()

tounzip_text = zip_text
unzip_text = rle_unzip(tounzip_text)
print(f'Разжатый текст: {unzip_text}\n')
print(f'Разжатие корректно: {tozip_text == unzip_text}\n')