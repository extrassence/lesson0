class house():
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors


    def go_to_floor(self, floor):
        if floor > self.floors or floor < 1:
            print(f'Этажа {floor} в доме {self.name} нет!')
            return
        print(f'Поднимаемся на лифте в доме {self.name}')
        for i in range (1, floor):
            print(i)
        print(f'Успешно добрались до {floor} этажа')


h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
h1.go_to_floor(5)
h2.go_to_floor(10)