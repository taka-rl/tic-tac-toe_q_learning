import random
from src.player import Player
from src.board import Board


class TicTacToeGame:
    def __init__(self) -> None:
        self.board = Board()
        self.player1 = None
        self.player2 = None

    def choose_game_mode(self) -> None:
        """Prompt to choose a game mode."""
        print("Choose a game mode:")
        print("1: Human vs Human")
        print("2: Human vs Computer")
        print("3: Computer vs Computer")
        # print("4: Human vs Agent")
        # print("5: Agent vs Computer")
        # print("6: Agent vs Agent")
        # print("7: Training the agent")
        mode = int(input("Enter mode number: "))

        if mode == 1:
            self.player1 = Player('human', 1)
            self.player2 = Player('human', 2)
        elif mode == 2:
            self.player1 = Player('human', 1)
            self.player2 = Player('computer', 2)
        elif mode == 3:
            self.player1 = Player('computer', 1)
            self.player2 = Player('computer', 2)
        else:
            print("Invalid choice, defaulting to Human vs Computer.")
            self.player1 = Player('human', 1)
            self.player2 = Player('computer', 2)

    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        self.choose_game_mode()

        # Randomly assign starting player
        current_turn = self.player1 if random.choice([True, False]) else self.player2

        while True:
            # Start the game
            self.game(current_turn)

            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()

            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round(self.board)
                # Switch turns
                current_turn = self.player2 if current_turn == self.player1 else self.player1
            else:
                print("Your input was not valid but I will assume that you want to play again!")

    def game(self, current_turn):
        print(f'----- Player{current_turn.get_player_number} turn -----')
        self.board.print_board()

        while True:  # Round
            if current_turn.get_player == 'human':
                move = current_turn.get_human_move()
            else:
                # computer
                move = current_turn.get_computer_move(self.board)

            self.board.submit_move(current_turn, move)
            self.board.print_board()

            if self.board.check_is_game_over(current_turn, move):
                print(f"Awesome. Player{current_turn.get_player_number} won the game!")
                break
            elif self.board.check_is_tie():
                print("It's a tie! Try again!")
                break

            # Switch turns
            current_turn = self.player2 if current_turn == self.player1 else self.player1

    @staticmethod
    def start_new_round(board):
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()
