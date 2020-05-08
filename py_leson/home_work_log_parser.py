import zipfile


class Log_parser():

    def __init__(self, file_name):
        self.file_name = file_name  # сам файл
        self.minuts = 37  # скорее всего надо прочитать первую строку и выписать значния
        self.hours = 19  # но это черновик
        self.month = 5  # и по этому пока просто вбил данные из первой строки
        self.years = 18
        self.line_prev = '[2018-05-14 19:37:47.873687] OK'
        self.count_ok = 0  # счётчик ок
        self.count_nok = 0  # счётчик нок

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def open_read(self):

        if self.file_name.endswith('.zip'):  # перестраховка
            self.unzip()
        f = open('file_1.txt', 'w', encoding='utf8')  # этот открываем для записи, через open - для практики
        with open(file_name, 'r', encoding='utf-8') as file:  # только для чтения
            for line in file:  # ищем по строкам
                if a == 1:  # решение если искать в мин, часах и т.д.
                    self._minutes(f, line)
                elif a == 2:
                    self._hours(f, line)
                elif a == 3:
                    self._months(f, line)
                else:
                    self._years(f, line)
        f.close()  # не забыть закрыть файл

    def _minutes(self, f, line):
        if int(line[15:17]) != self.minuts:  # вырезаем, переводим в инт и сравниваем
            f.write('{}]  {}\n'.format(self.line_prev[:17], self.count_nok))  # пишем
            self.minuts = int(line[15:17])  # переводим минуты
            self.count_ok = 0   # сбрасываем счётчик
            self.count_nok = 0
            self.line_prev = line  # предыдущую строку превращаем в текущую
        else:
            if line.endswith('NOK\n'):  # если строка заканчивается на нок
                self.count_nok += 1  # счётчик
            else:
                self.count_ok += 1

    def _hours(self, f, line):

        if int(line[12:14]) != self.hours:
            f.write('{}]  {}\n'.format(self.line_prev[:14], self.count_nok))
            self.hours = int(line[12:14])
            self.count_ok = 0
            self.count_nok = 0
            self.line_prev = line
        else:
            if line.endswith('NOK\n'):
                self.count_nok += 1
            else:
                self.count_ok += 1

    def _months(self, f, line):
        if int(line[6:8]) != self.month:
            f.write('{}]  {}\n'.format(self.line_prev[:8], self.count_nok))
            self.month = int(line[6:8])
            self.count_ok = 0
            self.count_nok = 0
            self.line_prev = line
        else:
            if line.endswith('NOK\n'):
                self.count_nok += 1
            else:
                self.count_ok += 1

    def _years(self, f, line):

        if int(line[3:5]) != self.years:
            f.write('{}]  {}\n'.format(self.line_prev[:5], self.count_nok))
            self.years = int(line[3:5])
            self.count_ok = 0
            self.count_nok = 0
            self.line_prev = line
        else:
            if line.endswith('NOK\n'):
                self.count_nok += 1
            else:
                self.count_ok += 1

    def act(self):
        self.open_read()  # вызывает функцию


file_name = 'events.txt'
a = 3  # 1 = минуты, 2 = часы, 3 = месяцы, 4 = года.
s = Log_parser(file_name='events.txt')
s.act()


