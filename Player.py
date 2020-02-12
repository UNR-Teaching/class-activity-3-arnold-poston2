from itertools import count
import re


class Player(object):
    _ids = count(1)

    def __init__(self, playerCharacter):
        # The single character to represent the players move on the player
        self.playerCharacter = playerCharacter
        if not self.check_valid_player():
            try:
                raise ValueError
            except ValueError:
                print("Invalid playerCharacter on Player creation")
                raise

        self.playerNumber = next(self._ids)

    def getMove(self):
        correctInputPattern = re.compile(r"\s*-?[0-9]\s*,\s*-?[0-9]\s*$")
        user_entered_data = input("Player {} enter in a move in the form (row, column)".format(self.playerNumber))
        column = -1
        row = -1
        if correctInputPattern.match(user_entered_data):
            user_entered_data = user_entered_data.replace(' ', '')
            row, column = user_entered_data.split(',')

            # Can break if column or row is not int
            column = int(column)
            row = int(row)

        while not self.check_valid_row_column(column, row):
            print("You have entered an invalid move, please try again.")
            user_entered_data = input("Player {} enter in a move in the form (row, column)".format(self.playerNumber))
            if correctInputPattern.match(user_entered_data):
                user_entered_data = user_entered_data.replace(' ', '')
                row, column = user_entered_data.split(',')

                # Can break if column or row is not int
                column = int(column)
                row = int(row)
        return row, column, self.playerCharacter

    def check_valid_row_column(self, column, row):
        if column < 0 or column > 2:
            return False
        if row < 0 or row > 2:
            return False
        return True

    def check_valid_player(self):
        return isinstance(self.playerCharacter, str) and len(self.playerCharacter) == 1