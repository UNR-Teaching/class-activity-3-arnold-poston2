import unittest
from GameDriver import GameDriver


class GameOverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GameDriver()

        self.staleMateBoard = [['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['O', 'X', 'O']]

        self.winnerRowBoard = [['X', 'O', 'O'],
                               ['X', 'X', 'X'],
                               ['O', 'X', 'X']]

        self.winnerColBoard = [['X', 'O', 'X'],
                               ['O', 'O', 'X'],
                               ['X', 'O', 'O']]

        self.rightDiagonalWinner = [['_', 'O', 'X'],
                                    ['O', 'X', 'X'],
                                    ['X', '_', 'O']]

        self.leftDiagonalWinner = [['X', 'O', 'O'],
                                   ['O', 'X', '_'],
                                   ['X', '_', 'X']]

    def test_at_game_start(self):
        self.assertFalse(self.driver.game_over())

    def test_stale_mate(self):
        self.driver.board.board = self.staleMateBoard
        self.assertTrue(self.driver.game_over())

    def test_winner_row_board(self):
        self.driver.board.board = self.winnerRowBoard
        self.assertTrue(self.driver.game_over())

    def test_winner_col_board(self):
        self.driver.board.board = self.winnerRowBoard
        self.assertTrue(self.driver.game_over())

    def test_right_diagonal_winner(self):
        self.driver.board.board = self.rightDiagonalWinner
        self.assertTrue(self.driver.game_over())

    def test_left_diagonal_winner(self):
        self.driver.board.board = self.leftDiagonalWinner
        self.assertTrue(self.driver.game_over())

if __name__ == '__main__':
    unittest.main()
