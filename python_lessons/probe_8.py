from datetime import datetime


class Parser():

    # инициализация
    def __init__(self, input_file, output_file, mode=1):
        self.input = input_file
        self.output = output_file
        self.mode = mode

        # режимы работы
        modes = {
            0: ('second', '%Y-%m-%d %H:%M:%S'),
            1: ('minute', '%Y-%m-%d %H:%M'),
            2: ('hour', '%Y-%m-%d %H'),
            3: ('day', '%Y-%m-%d'),
            4: ('month', '%Y-%m'),
            5: ('year', '%Y')
        }

        self.limit = modes[mode][0]
        self.time_format = modes[mode][1]

    # чтение входного файла
    def parse(self):
        with open(self.input, 'r', encoding='utf-8') as f:
            yield from f

    # запись в файл (в режиме дополнения)
    def write(self, s):
        with open(self.output, 'a', encoding='utf-8') as f:
            f.write(s)

    # фильтр строк содержащих 'NOK'
    def filter(self, s):
        if 'NOK' in s:
            return s

    # функция получающая дату из строки
    def get_date(self, s):
        try:
            date = datetime.strptime(s[1:s.index('.')], '%Y-%m-%d %H:%M:%S')
        except AttributeError:
            return None
        except ValueError:
            return None

        return date

    # старт парсера
    def start(self):

        # генератор строк из входного файла
        g = self.parse()

        # счетчик
        count = 1
        # предыдущая строка
        prev = None

        # цикл
        while True:
            # получает строку от генератора
            try:
                i = next(g)
            # если строк больше нет
            # записывает данные из последней строки в выходной файл
            except StopIteration:
                if self.get_date(prev):
                    self.write(self.get_date(prev).strftime(self.time_format) + ' NOK ' + str(count) + '\n')
                break

            # фильтрует строки по наличию 'NOK'
            if self.filter(i):

                # если найдена первая строка с нормальной датой
                # записывает ее как предыдущую и продолжает цикл
                if prev is None:
                    if self.get_date(i):
                        prev = i

                # если предыдущая строка есть
                else:
                    # проверяет дату текущей строки
                    if self.get_date(i):
                        # сравнивает даты текущей и предыдущей
                        # если равны увеличивает счетчик
                        # назначает текущую строку предыдущей
                        if getattr(self.get_date(i), self.limit) == getattr(self.get_date(prev), self.limit):
                            count += 1
                            prev = i
                        # если не равны
                        # записывает данные предыдущей строки в файл
                        # делает счетчик равным 1
                        # назначает текущую строку предыдущей
                        else:
                            self.write(self.get_date(prev).strftime(self.time_format) + ' NOK ' + str(count) + '\n')
                            count = 1
                            prev = i


# запуск в режиме по умолчанию
parser = Parser('events.txt', 'output.txt')
parser.start()

# запуск в выбранном режиме (0 - секунды, 1 - минуты, 2 - часы, 3 - дни, 4 - месяцы, 5 - годы)
# parser = Parser('events.txt', 'output.txt', 2)
# parser.start()
