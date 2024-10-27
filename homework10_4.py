import random
import time
from queue import Queue
import threading


class Table:

    def __init__(self, num):
        self.number = num
        self.guest = None

class Guest(threading.Thread):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:

    def __init__(self, *args):
        self.tables = args
        self.guestqueue = Queue()
        self.tablequeue = Queue() # Сделал очередь столов, чтоб их можно было не просто нумеровать, но и дать имя
        self.occupied = 0

    def guest_arrival(self, *guests):
        self.guests = guests
        for g in self.guests:      # гости выстраиваются в очередь
            if not g.is_alive():
                self.guestqueue.put(g)
            print(f'Гость {g.name} ждёт своей очереди')
        print('Кафе открывается!')
        for t in self.tables:      # Первые гости рассаживаются по свободным столикам
            if t.guest == None:
                self.tablequeue.put(t)
        while not self.tablequeue.empty():
                t = self.tablequeue.get()
                t.guest = self.guestqueue.get()
                self.occupied += 1 # счетчик занятых столов
                print(f'{t.guest.name} сел перекусить за стол {t.number}')
                t.guest.start() # ест

    def discuss_guests(self):
        while not cafe.guestqueue.empty():
            for t in self.tables:          # Всё время проверяем все столики, не освободился ли, если освободился,
                if not t.guest.is_alive(): # тогда снимаем со стола табличку с именем
                    print(f'Гость {t.guest.name} закончил приём пищи и освободил стол {t.number}')
                    t.guest = None
                    self.occupied -= 1
                    self.tablequeue.put(t)
            while (not cafe.tablequeue.empty()) and (not cafe.guestqueue.empty()): # если есть столы и очередь
                t = self.tablequeue.get()
                t.guest = self.guestqueue.get()
                self.occupied += 1
                print(f'{t.guest.name} сел перекусить за стол {t.number}')
                t.guest.start()
        while self.occupied > 0: # Очередь закончилась, ждем когда все доедят
            for t in self.tables:
                if not t.guest == None:
                    if not t.guest.is_alive():
                        print(f'Гость {t.guest.name} закончил приём пищи и освободил стол {t.number}')
                        self.occupied -= 1
                        t.guest = None

# Создание столов
tables = [Table(number) for number in (1, 2, 3, "VIP", "Служебный", "в туалете")]
# Имена гостей
guests_names = [
'Мария', 'Олег', 'Вахтанг', 'Сергей', 'Дарья', 'Арман',
'Виктория', 'Никита', 'Галина', 'Павел', 'Илья', 'Александра'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

