import random
from player import Player
from board import Board


class TicTacToeGame:
    def __init__(self) -> None:
        self.board = Board()
        self.player = Player()
        self.computer = Player(False)

    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        while True:  # Game
            # set the play order
            if random.randint(0, 1):
                # player first
                self.game(player_starts=True)
            else:
                # computer first
                self.game(player_starts=False)
            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()

            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round(self.board)
            else:
                print("Your input was not valid but I will assume that you want to play again!")

    def game(self, player_starts):
        player1, player2 = (self.player, self.computer) if player_starts else (self.computer, self.player)
        if player_starts:
            print("----- You are player1 -----")
        else:
            print("----- You are player2 -----")

        while True:  # Round
            # first player
            player1_move = player1.get_move() if player1.is_human else player1.get_computer_move(self.board)
            self.board.submit_move(player1, player1_move)
            self.board.print_board()

            if self.board.check_is_game_over(player1, player1_move):
                print("Awesome. player1 won the game!")
                break
            elif self.board.check_is_tie():
                print("It's a tie! Try again!")
                break
            else:
                # second player
                player2_move = player2.get_move() if player2.is_human else player2.get_computer_move(self.board)
                self.board.submit_move(player2, player2_move)
                self.board.print_board()

                if self.board.check_is_game_over(player2, player2_move):
                    print("Awesome. player2 won the game!")
                    break
                elif self.board.check_is_tie():
                    print("It's a tie! Try again!")
                    break

    @staticmethod
    def start_new_round(board):
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()
