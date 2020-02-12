import unittest
from Board import Board
from GameDriver import GameDriver


class GameOverIntegrationTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = GameDriver()

        self.driver.board = Board()
        self.driver.board.board = [['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', 'X', 'O']]

    def test_game_over_full_board(self):
        self.assertTrue(self.driver.game_over())
        self.assertTrue(self.driver.board.check_full_board())
