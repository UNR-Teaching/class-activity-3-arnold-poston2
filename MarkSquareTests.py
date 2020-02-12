import unittest
from Board import Board


class MarkSquareTests(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyTicTacToe = Board()
        self.almostFilledTicTacToe = Board()
        self.beforeAfterTest = Board()

        self.almostFilledTicTacToe.board = [['X', 'O', 'X'],
                                            ['X', '_', 'O'],
                                            ['O', 'X', 'O']]

        self.beforeMarkSquareBoard = [['_', 'O', 'X'],
                                      ['X', 'O', 'O'],
                                      ['O', 'X', '_']]

        self.afterMarkSquareBoard = [['X', 'O', 'X'],
                                     ['X', 'O', 'O'],
                                     ['O', 'X', '_']]

    def test_valid_row_0_column_0(self):
        self.assertTrue(self.emptyTicTacToe.mark_square(0, 0, 'X'))

    def test_invalid_row_0_column_0(self):
        self.assertFalse(self.almostFilledTicTacToe.mark_square(0, 0, 'X'))

    def test_board_change_valid_row_0_column_0(self):
        self.emptyTicTacToe.mark_square(0, 0, 'O')
        self.assertTrue(self.emptyTicTacToe.board[0][0] == 'O')

    def test_board_change_invalid_row_0_column_0(self):
        self.almostFilledTicTacToe.mark_square(0, 0, 'O')
        self.assertFalse(self.almostFilledTicTacToe.board[0][0] == 'O')

    def test_board_change_correct_without_changing_anything_else_on_the_board(self):
        self.beforeAfterTest.board = self.beforeMarkSquareBoard
        self.beforeAfterTest.mark_square(0, 0, 'X')
        self.assertListEqual(self.beforeAfterTest.board, self.afterMarkSquareBoard)

if __name__ == '__main__':
    unittest.main()
