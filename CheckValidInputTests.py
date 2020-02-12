import unittest
from Player import Player


class CheckValidPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.playerO = Player('O')

    def test_valid_input(self):
        self.assertTrue(self.playerO.check_valid_input("1, 1"))

    def test_random_string(self):
        self.assertFalse(self.playerO.check_valid_input("asdlkfadfjha;sdfalskdjhasldfkjalskhdj"))

    def test_out_of_col_range_input(self):
        self.assertTrue(self.playerO.check_valid_input("1, 5"))


if __name__ == '__main__':
    unittest.main()
