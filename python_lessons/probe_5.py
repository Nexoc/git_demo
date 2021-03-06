# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    food = 50
    money = 100
    dust = 0
    food_for_cat = 30

    def __init__(self):
        pass

    def __str__(self):
        return 'В доме осталось еды {}, денег {}, уровень загрязнения {}, еды для питомцев {}'.format(
            self.food, self.money, self.dust, self.food_for_cat)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = House()

    def __str__(self):
        return 'Я - {}, сытость {}, счастья {}'.format(
            self.name, self.fullness, self.happiness)

    def eat(self):
        if House.food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 40
            House.food -= 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def act(self):
        self.happiness -= 10
        self.fullness -= 10
        if House.dust >= 90:
            self.happiness -= 10
            cprint('{} очень грязно, настроение плохое'.format(self.name), color='red')
        elif self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        elif self.happiness <= 0:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return
        elif self.fullness < 30:
            self.eat()
            return
        else:
            self.happiness += 5
            Cat.playing(self.name)
            return


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        House.money += 150

    def gaming(self):
        cprint('{} весь день играл'.format(self.name), color='green')
        self.happiness += 20

    def act(self):
        super().act()
        if self.happiness < 30:
            self.gaming()
        else:
            self.work()


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if 100 <= House.money <= 250:
            cprint('{} сходила в магазин'.format(self.name), color="magenta")
            House.food += 100
            House.money -= 100
        elif House.money >= 250:
            cprint('{} сходила в магазин'.format(self.name), color="magenta")
            House.food += 250
            House.money -= 250
        else:
            cprint('{} денег на еду нет'.format(self.name), color='red')

    def shoping_for_cats(self):
        if self.house.money >= 30:
            cprint('{} сходила в магазин за едой питомцам'.format(self.name), color="magenta")
            House.food_for_cat += 50
            House.money -= 50
        else:
            cprint('{} нет денег на еду питомцам'.format(self.name), color='red')

    def buy_fur_coat(self):
        cprint('{} купила шубу'.format(self.name), color='green')
        self.happiness += 60
        House.money -= 350

    def clean_house(self):
        cprint('{} весь день убиралась'.format(self.name), color='green')
        House.dust = 0

    def act(self):
        House.dust += 5
        super().act()
        if House.food < 70:
            self.shopping()
        elif House.dust > 80:
            self.clean_house()
        elif House.food_for_cat < 40:
            self.shoping_for_cats()
        elif self.happiness < 30:
            if 450 < House.money < 800:
                self.buy_fur_coat()
        elif House.money > 800:
            self.buy_fur_coat()
            self.buy_fur_coat()


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def eat(self):
        if House.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            House.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} весь день спал'.format(self.name), color='yellow')

    def act(self):
        self.fullness -= 10
        if self.fullness < 30:
            self.eat()
        else:
            self.sleep()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = House()

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if House.food_for_cat >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            House.food_for_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        print('{} спал весь день'.format(self.name))

    def soil(self):
        House.dust += 5
        cprint('{} драл обои'.format(self.name), color='yellow')

    def playing(self):
        cprint('драл обои', color='yellow')

    def act(self):
        self.fullness -= 10
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        elif self.fullness < 20:
            self.eat()
            return
        dice = randint(1, 2)
        if dice == 1:
            self.sleep()
        else:
            self.soil()


home = House()
citizens = [
    Husband(name='Марат'),
    Wife(name='Люда'),
    Child(name='Минзакир'),
    Cat(name='Мурзик'),
    Cat(name='Черныш'),
    Cat(name='Барсик')
]


for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    for citizen in citizens:
        citizen.act()
    for citizen in citizens:
        print(citizen)
    cprint(home, color='cyan')

# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
#


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

