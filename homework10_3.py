from threading import Thread, Lock
from time import sleep
from random import randint



class Bank:
    def __init__(self):
        self.balance = 0
        self.still_deposit = True

    def deposit(self):
        for i in range (1, 101):
            inc = randint(50, 500)
            if self.balance > 500 and lock.locked():
                lock.release()
            sleep(0.05)
            self.balance += inc
            print(f'{i}. Пополнение счета на {inc} бабок, остаток {self.balance} бабок\n', end='')
        self.still_deposit = False

    def take(self):
        for i in range (1, 101):
            dec = randint(50, 500)
            while self.balance < dec:
                if self.still_deposit:
                    print(f'На счету: {self.balance} бабок, невозможно снять {dec} бабок\n', end='')
                lock.acquire()
                if not self.still_deposit: #Если поток депозитов закончился, то некому будет
                    lock.release()         #открыть запертый поток снятия
                    print('Депозиты закончились, включен механизм кредитования\n', end='')
                    break
            sleep(0.05)
            self.balance -= dec
            print(f'.{i} Снятие со счета {dec} бабок, остаток {self.balance} бабок \n', end='')




bk = Bank()
lock = Lock()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
