# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.

import zipfile
from pprint import pprint
from random import randint

# file_name = 'voyna-i-mir.txt'

# stat = {}
#
#
# # if file_name.endswith('.zip'):
# #     zfile = zipfile.ZipFile(file_name, 'r')
#
# with open(file_name, 'r', encoding='cp1251') as file:
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 if char in stat:
#                     stat[char] += 1
#                 else:
#                     stat[char] = 1


# d = sorted(stat)
# d.sort()
# for i in d:
#     print(i, ':', stat[i])

# d = sorted(stat)
# d.sort(reverse=True)
# for i in d:
#     print(i, ':', stat[i])

# d = sorted(stat)
# d.sort(reverse=True)
# for i in d:
#     print(i, ':', stat[i])


# d = sorted(stat)
# print(d)
# c = 0
# print('+{txt:-^60}+'.format(txt='+'))
# print('|{letter: ^29}'.format(letter='буква'), end='')
# print('|{count: ^30}|'.format(count='частота'))
# print('+{txt:-^60}+'.format(txt='+'))
# for key, value in d.items():
#     c += value
#     print(f'|{key: ^29}|{value: ^30}|')
# print('+{txt:-^60}+'.format(txt='+'))
# print('|{letter: ^29}'.format(letter='итого'), end='')
# print('|{count: ^30}|'.format(count=c))
# print('+{txt:-^60}+'.format(txt='+'))


class Statistic:
    def __init__(self, file_name):
        self.stat = {}
        self.file_name = file_name

    def byletter(self):
        c = 0
        print('+{txt:-^60}+'.format(txt='+'))
        print('|{letter: ^29}'.format(letter='буква'), end='')
        print('|{count: ^30}|'.format(count='частота'))
        print('+{txt:-^60}+'.format(txt='+'))
        for i in sorted(self.stat):
            c += self.stat[i]
            print(f'|{i: ^29}|{self.stat[i]: ^30}|')
        print('+{txt:-^60}+'.format(txt='+'))
        print('|{letter: ^29}'.format(letter='итого'), end='')
        print('|{count: ^30}|'.format(count=c))
        print('+{txt:-^60}+'.format(txt='+'))

    def byletter_reverse(self):
        c = 0
        print('+{txt:-^60}+'.format(txt='+'))
        print('|{letter: ^29}'.format(letter='буква'), end='')
        print('|{count: ^30}|'.format(count='частота'))
        print('+{txt:-^60}+'.format(txt='+'))
        for i in sorted(self.stat, reverse=True):
            c += self.stat[i]
            print(f'|{i: ^29}|{self.stat[i]: ^30}|')
        print('+{txt:-^60}+'.format(txt='+'))
        print('|{letter: ^29}'.format(letter='итого'), end='')
        print('|{count: ^30}|'.format(count=c))
        print('+{txt:-^60}+'.format(txt='+'))

    def bycount(self):
        for i in sorted(self.stat.items(), key=lambda a: (a[1], a[0])):
            print(i)

    def bycount_reverse(self):
        for i in sorted(self.stat.items(), key=lambda a: (a[1], a[0]), reverse=True):
            print(i)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def open_read(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
        return self.stat

    def act(self):
        self.open_read()


file_name = 'voyna-i-mir.txt'
s = Statistic(file_name='voyna-i-mir.txt')
s.act()
# s.byletter()
# s.byletter_reverse()
# s.bycount
# s.bycount_reverse()
