import unittest
from GameDriver import GameDriver


class CheckNextPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GameDriver()

    def test_O_player(self):
        self.assertEqual(self.driver.current_player, 0)

    def test_next_player(self):
        self.driver.next_player()
        self.assertEqual(self.driver.current_player, 1)

    def test_1000_next_player(self):
        for _ in range(100):
            self.driver.next_player()
        self.assertEqual(self.driver.current_player, 0)


if __name__ == '__main__':
    unittest.main()
