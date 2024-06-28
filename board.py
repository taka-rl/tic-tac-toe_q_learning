class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    @staticmethod
    def print_board_with_positions():
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
            return True
        else:
            print("This position is already taken. Please enter another one.")
            return False

    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move)
                 or (self.check_column(player, last_move)
                     or (self.check_diagnal(player)
                         or (self.check_antidiagnal(player))))))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]  # ["0", 0, X]
        return board_row.count(player.marker) == 3

    def check_column(self, player, last_move):
        markers_count = 0
        column_index = last_move.get_column()

        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagnal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_antidiagnal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_is_tie(self):
        empty_counter = 0
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)
        return empty_counter == 0

    def reset_board(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    # RL
    def get_state(self, current_player):
        # Convert the board to a tuple and add the current player's turn
        return tuple(tuple(row) for row in self.game_board), current_player

    def get_possible_moves(self):
        possible_actions = []
        for cols in range(0, 3):
            for rows in range(0, 3):
                if self.game_board[cols][rows] == 0:
                    if cols == 0:
                        num = rows + 1
                    elif cols == 1:
                        num = rows + 1 + 3
                    elif cols == 2:
                        num = rows + 1 + 6
                    possible_actions.append(num)
        return possible_actions

