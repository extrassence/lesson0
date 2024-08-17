class House():
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, этажность: {len(self)}'  # во, так тоже можно оказывается

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

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
