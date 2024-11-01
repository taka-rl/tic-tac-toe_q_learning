import random
from move import Move
from board import Board


class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True) -> None:
        self._is_human = is_human
        self._marker = Player.PLAYER_MARKER if is_human else Player.COMPUTER_MARKER

    @property
    def is_human(self) -> bool:
        return self._is_human

    @property
    def marker(self) -> str:
        return self._marker

    def get_move(self) -> Move:
        if self._is_human:
            return self.get_human_move()
        else:
            # For computer moves, we now need to pass the board instance
            raise ValueError("get_move() should not be called directly for the computer. Use get_computer_move(board).")

    @staticmethod
    def get_human_move() -> Move:
        while True:
            user_input = int(input("Please enter your move(1-9):"))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move

    @staticmethod
    def get_computer_move(board) -> Move:
        # random_choice = random.choice(range(1, 10))
        # move = Move(random_choice)
        available_actions = board.get_possible_moves()
        random_choice = random.choice(available_actions)
        move = Move(random_choice)
        print("Computer move (1-9):", move.value)
        return move
