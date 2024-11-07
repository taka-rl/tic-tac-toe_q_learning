import random
from src.move import Move


class Player:
    FIRST_PLAYER_MARKER = "X"
    SECOND_PLAYER_MARKER = "O"

    def __init__(self, player: str, num: int) -> None:
        self._player = player
        self._num = num
        if num == 1:
            self._marker = Player.FIRST_PLAYER_MARKER
        else:
            self._marker = Player.SECOND_PLAYER_MARKER

    @property
    def get_player(self) -> str:
        return self._player

    @property
    def get_player_number(self) -> int:
        return self._num

    @property
    def marker(self) -> str:
        return self._marker

    def get_move(self) -> Move:
        if self._player == 'human':
            return self.get_human_move()
        else:
            # For computer moves, we now need to pass the board instance
            raise ValueError("get_move() should not be called directly for the computer. Use get_computer_move(board).")

    @staticmethod
    def get_human_move() -> int:
        while True:
            user_input = int(input("Please enter your move(1-9):"))
            move = user_input
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move

    @staticmethod
    def get_computer_move(board) -> int:
        # random_choice = random.choice(range(1, 10))
        # move = Move(random_choice)
        available_actions = board.get_possible_moves()
        random_choice = random.choice(available_actions)
        move = random_choice
        print("Computer move (1-9):", move)
        return move
