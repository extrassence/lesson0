import unittest
from homework12_4logs import Runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner.log', encoding='UTF-8',
                            format="%(asctime)s | %(levelname)s | %(message)s")

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_walk(self):
        try:
            runner = Runner(name=True, speed=5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as exc:
            logging.warning(f'{exc} - Неверный тип данных для объекта Runner')
        except ValueError as exc:
            logging.warning(f'{exc} - Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Отключен')
    def test_run(self):
        try:
            runner = Runner(name="Петя", speed=-10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning(f'{exc} - Неверный тип данных для объекта Runner')
        except ValueError as exc:
            logging.warning(f'{exc} - Неверная скорость для Runner')

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
