class Figure:

    def __init__(self, colr, *sides):
        Figure.sides_count = len(sides)
        self.__color = list(colr)
        self.__sides = list(sides)
        self.filled = self.__is_valid_color(*colr)
        if not self.__is_valid_sides(*sides):
            self.__sides = list((1,) * self.sides_count)

    def __is_valid_color(self, *color):
        for i in color:
            if not isinstance(i, int):
                return False
            if i < 0 or i > 255:
                return False
        return True

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        cc = (r, g, b)
        if self.__is_valid_color(*cc):
            self.__color = list(cc)
            self.filled = True

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for i in sides:
            if i < 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, colr, side):
        Figure.__init__(self, colr, side)
        self.__radius = side / (2 * 3.1415926538)

    def get_square(self):
        return self.__radius ** 2 * 3.1415926538


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colr, *sides):
        Figure.__init__(self, colr, *sides)

    def get_square(self):
        pp = sum(self.get_sides()) / 2
        return (pp * (pp - self.get_sides()[0]) * (pp - self.get_sides()[1]) * (pp - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, colr, side):
        sides = list((side,) * 12)
        Figure.__init__(self, colr, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((0, 1, 0), 10, 10, 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

print(triangle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())
