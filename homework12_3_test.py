import unittest
from homework12_3_main import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True
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

#    @unittest.skipIf(is_frozen, 'Отключен')  Ого, оказывается если перед setUp это вставить, то отключатся все.
    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_race_usain_nick(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertTrue(self.__class__.all_results[self.__class__.index][1].name == "Usain")
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Nick")

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_race_andrey_nick(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertTrue(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Nick")

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_full_race(self):
        self.__class__.index += 1
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][2].name == "Usain")
        self.assertTrue(self.__class__.all_results[self.__class__.index][3].name == "Nick")

    @unittest.skipIf(not is_frozen, 'Отключен')  # один решил оставить
    def test_logic_error(self):
        self.__class__.index += 1
        tournament = Tournament(18, self.runner2, self.runner1, self.runner3)
        self.__class__.all_results[self.__class__.index] = tournament.start()
        self.assertFalse(self.__class__.all_results[self.__class__.index][1].name == "Andrey")
        self.assertFalse(self.__class__.all_results[self.__class__.index][2].name == "Usain")
        self.assertTrue(self.__class__.all_results[self.__class__.index][3].name == "Nick")


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        pass

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_walk(self):
        runner = Runner("Коля")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_run(self):
        runner = Runner("Петя")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_challenge(self):
        runner1 = Runner("Вася")
        runner2 = Runner("Навуходоносор")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
