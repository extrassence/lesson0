class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if cls.houses_history is None:
            cls.houses_history = []
        else:
            cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, этажность: {len(self)}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        else:
            print(f'Нельзя сравнивать {self.name} с {other}')

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        else:
            print(f'Нельзя прибавить {other} к {self.name}')

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        else:
            print(f'Нельзя прибавить {other} к {self.name}')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to_floor(self, floor):
        if floor > self.floors or floor < 1:
            print(f'Этажа {floor} в доме {self.name} нет!')
            return
        print(f'Поднимаемся на лифте в доме {self.name}')
        for i in range(1, floor):
            print(i)
        print(f'Успешно добрались до {floor} этажа')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
