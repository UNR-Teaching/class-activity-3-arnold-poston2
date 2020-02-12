
class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        if self.board[row][column] != '_':
            return False

        self.board[row][column] = player

        return True
        pass

    def check_full_board(self):
        for row in self.board:
            for character in row:
                if character == '_':
                    return False
        return True

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        for i in range(0, 3):
            if (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) \
                    and (self.board[i][0] != '_'):
                return self.board[i][0]
            if (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) \
                    and (self.board[0][i] != '_'):
                return self.board[0][i]

        if (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]) \
                and (self.board[1][1] != '_'):
            return self.board[0][0]
        if (self.board[2][0] == self.board[1][1]) and (self.board[0][2] == self.board[1][1]) \
                and (self.board[1][1] != '_'):
            return self.board[2][0]

        return False
        pass

    def print(self):
        for row in self.board:
            for element in row:
                print(element + " ", end='')
            print('')

