from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, nam, pwr):
        super().__init__()
        self.enemies = 100
        self.name = nam
        self.strength = pwr
        self.days = 0
        print(f'Атака на замок рыцаря {self.name}!')



    def run(self):
        while self.enemies > 0:
            self.enemies -= self.strength
            self.days += 1
            print(f'{self.name} День сражений: {self.days}, врагов осталось: {self.enemies}', end='\n')
            sleep(1)
        print(f'Сражение длилось {self.days} дней. {self.name} одержал победу!', end='\n')
        #return self.enemies


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()