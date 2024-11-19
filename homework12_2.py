import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            maxdistance = 0
            for participant in self.participants:  # отдельный цикл для пробежки за единицу времени для всех
                participant.run()
                if participant.distance > maxdistance:
                    maxdistance = participant.distance  # запоминаем кто дальше убежал

            for participant in self.participants:
                if participant.distance >= self.full_distance and participant.distance == maxdistance:  # плюс условие
                    # с этим небольшим условием тот, кто медленнее, не займет первое место, если его первым проверят.
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Я замучался выполнять это условие, результат можете наблюдать ниже
        # Да, это словарь, в котором хранятся результаты ВСЕХ тестов, которые тоже словари
        # И он объявлен именно в setUpClass, как заказывали.
        cls.index = 0

    @classmethod
    def tearDownClass(cls):
        print('\n')
        for key, value in cls.all_results.items():
            print(f'------------- {key} --------------')
            for key1, value1 in value.items():
                print(f'{key1}: {value1}')

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    def test_race_usain_nick(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertTrue(self.__class__.all_results[self.__class__.index][1].name == "Usain")
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Nick")

    def test_race_andrey_nick(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertTrue(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Nick")

    def test_full_race(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][2].name == "Usain")
        self.assertTrue(self.__class__.all_results[self.__class__.index][3].name == "Nick")

    def test_logic_error(self):
        self.__class__.index += 1
        tournament = Tournament(18, self.runner2, self.runner1, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][2].name == "Usain")
        self.assertTrue(self.__class__.all_results[self.__class__.index][3].name == "Nick")


if __name__ == '__main__':
    unittest.main()
