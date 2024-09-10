class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, own, mdl, colr, pwr):
        self.owner = own
        self.__model = mdl
        self.__engine_power = pwr
        self.__color = colr

    def get_model(self):
        print("Модель: ", self.__model)

    def get_horsepower(self):
        print("Мощность двигателя: ", self.__engine_power)

    def get_color(self):
        print("Цвет: ", self.__color)

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        if self.__COLOR_VARIANTS.count(new_color.lower()) > 0:
            self.__color = new_color.lower()
            print(f'{self.__model} перекрашена в {new_color}')
        else:
            print(f'{self.__model} нельзя перекрасить в {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()