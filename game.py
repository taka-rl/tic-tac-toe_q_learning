"""
・agent, computer(random) player can randomly play first or second.先手、後手
・ask to input a number again if the number has been already occupied

"""


import random
from player import Player
from board import Board


class TicTacToeGame:
    
    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        board = Board()
        player = Player()
        computer = Player(False)

        while True:  # Game
            # set the play order
            if random.randint(0, 1):
                # player first
                print("----- You are player1 -----")
                self.game(board, [player, computer])
            else:
                # computer first
                print("----- You are player2 -----")
                self.game(board, [computer, player])

            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()
            
            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again!")

    @staticmethod
    def game(board, players):
        player1, player2 = players
        while True:  # Round
            player1_move = player1.get_move()
            board.submit_move(player1, player1_move)
            board.print_board()

            if board.check_is_game_over(player1, player1_move):
                print("Awesome. player1 won the game!")
                break
            elif board.check_is_tie():
                print("It's a tie! Try again!")
                break
            else:
                player2_move = player2.get_move()
                board.submit_move(player2, player2_move)
                board.print_board()

                if board.check_is_game_over(player2, player2_move):
                    print("Awesome. player2 won the game!")
                    break
                elif board.check_is_tie():
                    print("It's a tie! Try again!")
                    break

    @staticmethod
    def start_new_round(board):
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.start()
