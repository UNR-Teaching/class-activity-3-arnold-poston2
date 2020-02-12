import unittest
from Player import Player


class CheckValidPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.playerO = Player('X')

    def test_O_player(self):
        self.assertTrue(self.playerO.check_valid_player())

    def test_integer_player(self):
        self.assertRaises(ValueError, Player, 2)


if __name__ == '__main__':
    unittest.main()
