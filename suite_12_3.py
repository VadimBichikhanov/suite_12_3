import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем объект TestSuite
suite = unittest.TestSuite()
# Создаем объект TestLoader
loader = unittest.TestLoader()
# Добавляем тесты RunnerTest и TournamentTest в TestSuite

# Добавляем тесты RunnerTest и TournamentTest в TestSuite
suite.addTest(loader.loadTestsFromTestCase(RunnerTest))
suite.addTest(loader.loadTestsFromTestCase(TournamentTest))

# Создаем объект TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем TestSuite
runner.run(suite)