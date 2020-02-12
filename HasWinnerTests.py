import unittest
from Board import Board


class HasWinnerTests(unittest.TestCase):
    def setUp(self):
        self.tictactoe = Board()

        self.staleMateBoard = [['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['O', 'X', 'O']]

        self.winnerRowBoard = [['X', 'O', 'O'],
                                 ['X', 'X', 'X'],
                                 ['O', 'X', 'X']]

        self.winnerColBoard = [['X', 'O', 'X'],
                               ['O', 'O', 'X'],
                               ['X', 'O', 'O']]

        self.emptyBoard = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]

        self.rightDiagonalWinner = [['_', 'O', 'X'],
                                    ['O', 'X', 'X'],
                                    ['X', '_', 'O']]

        self.leftDiagonalWinner = [['X', 'O', 'O'],
                                    ['O', 'X', '_'],
                                    ['X', '_', 'X']]

    def test_stalemate(self):
        self.tictactoe.board = self.staleMateBoard
        self.assertFalse(self.tictactoe.has_winner())

    def test_row_winner(self):
        self.tictactoe.board = self.winnerRowBoard
        self.assertEqual(self.tictactoe.has_winner(), 'X')

    def test_col_winner(self):
        self.tictactoe.board = self.winnerColBoard
        self.assertEqual(self.tictactoe.has_winner(), 'O')

    def test_empty_board_no_winner(self):
        self.tictactoe.board = self.emptyBoard
        self.assertFalse(self.tictactoe.has_winner())

    def test_right_diagonal_winner(self):
        self.tictactoe.board = self.rightDiagonalWinner
        self.assertEqual(self.tictactoe.has_winner(), 'X')

    def test_left_diagonal_winner(self):
        self.tictactoe.board = self.leftDiagonalWinner
        self.assertEqual(self.tictactoe.has_winner(), 'X')


if __name__ == '__main__':
    unittest.main()
