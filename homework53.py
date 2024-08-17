class House:
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

    def go_to_floor(self, floor):
        if floor > self.floors or floor < 1:
            print(f'Этажа {floor} в доме {self.name} нет!')
            return
        print(f'Поднимаемся на лифте в доме {self.name}')
        for i in range(1, floor):
            print(i)
        print(f'Успешно добрались до {floor} этажа')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
