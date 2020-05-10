# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 10
            self.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходила на работу'.format(self.name), color='blue')
        self.money += 50
        self.fullness -= 10

    def play_dolls(self):
        cprint('{} играла в куклы'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            if self.food > 10:
                cprint('{} сходила в магазин'.format(self.name), color="magenta")
                self.food += 50
                self.money -= 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} очень хочет кушать'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 50:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dolls()


daryna = Man(name='Дарина')
for day in range(1, 366):
    print('============ день {} ============='.format(day))
    daryna.act()
    print(daryna)

