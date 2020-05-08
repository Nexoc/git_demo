# -*- coding: utf-8 -*-

text_1 = []  # value
text_2 = []  # key
with open('1.txt', mode='r', encoding='utf8') as file:  # подставте сами кодировку
    for line in file:
        key, value = line.split()  # value
        text_1.append(value)

with open('2.txt', mode='r', encoding='utf8') as file_2:
    for key in file_2:
        key = key.rstrip()  # key
        text_2.append(key)

with open('out.txt', mode='w', encoding='utf8') as file_3:
    a = zip(text_2, text_1)
    for k in a:
        file_3.write(f'{k[0]}, {k[1]}\n')


