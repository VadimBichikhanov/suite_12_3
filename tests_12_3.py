import unittest

def skip_frozen_tests(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen_tests
    def test_challenge(self):
        self.assertTrue(True)

    @skip_frozen_tests
    def test_run(self):
        self.assertTrue(True)

    @skip_frozen_tests
    def test_walk(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_frozen_tests
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_frozen_tests
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_frozen_tests
    def test_third_tournament(self):
        self.assertTrue(True)