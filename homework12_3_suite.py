import unittest
from homework12_3_main import Runner, Tournament
from homework12_3_test import RunnerTest, TournamentTest

TournamentTestAll = unittest.TestSuite()
TournamentTestAll.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
TournamentTestAll.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TournamentTestAll)