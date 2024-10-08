from random import choice

class MysticBall:

    def __init__(self, *choices):
        self.words = choices

    def __call__(self):
        return choice(self.words)

def get_advanced_writer(filename):
    def writeall(*pars):
        file = open(filename, 'w', encoding='utf-8')
        for i in pars:
            if type(i) == str:
                file.write(i+'\n')
            else:
                file.write(str(i)+'\n')
        file.close()
    return writeall


first = 'Мама мыла раму'
second = 'Рамена мало было'
print (list(map(lambda x, y: x == y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Любит', "Не любит", "Плюнет", "Поцелует", "К сердцу прижмет", "К черту пошлет")
print(first_ball())
print(first_ball())
print(first_ball())
