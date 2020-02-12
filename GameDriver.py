
from Board import Board
from Player import Player


class GameDriver(object):

    def __init__(self):
        self.board = Board()
        self.players = [Player('X'), Player('O')]
        self.current_player = 0
        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """

        while not self.game_over():
            self.board.print()
            row, column, player_symbol = self.get_current_player().getMove()
            while self.board.mark_square(column, row, player_symbol) is not True:
                print("That space is taken.")
                self.board.print()
                row, column, player_symbol = self.get_current_player().getMove()

            self.next_player()

        self.end_game()

    def end_game(self):

        if not self.board.has_winner:
            print("Stalemate :(")
        else:
            winner_symbol = self.board.has_winner
            for player in self.players:
                if player.playerCharacter == winner_symbol:
                    print("Player {} Wins!".format(player.playerCharacter))
                    return

    def game_over(self):
        if self.board.has_winner() or self.board.check_full_board():
            return True
        return False

    def get_current_player(self):
        return self.players[self.current_player]

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)
