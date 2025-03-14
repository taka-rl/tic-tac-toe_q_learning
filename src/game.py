import random
import pandas as pd
from src.player import Player
from src.board import Board
from src.move import Move
from src.rl import QLearningAgent


class TicTacToeGame:
    WIN = 1
    TIE = 0.5
    LOSE = -1

    def __init__(self, learning_rate=0.1, discount_factor=0.9, epsilon=0.1) -> None:
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.q_agent = QLearningAgent(learning_rate=learning_rate, discount_factor=discount_factor, epsilon=epsilon)

    def choose_game_mode(self) -> None:
        """Prompt to choose a game mode."""
        print("Choose a game mode:")
        print("1: Human vs Human")
        print("2: Human vs Computer")
        print("3: Computer vs Computer")
        print("4: Human vs Agent")
        print("5: Agent vs Computer")
        print("6: Agent vs Agent")
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
        elif mode == 4:
            self.player1 = Player('human', 1)
            self.player2 = Player('agent', 2)
        elif mode == 5:
            self.player1 = Player('agent', 1)
            self.player2 = Player('computer', 2)
        elif mode == 6:
            self.player1 = Player('agent', 1)
            self.player2 = Player('agent', 2)
        else:
            print("Invalid choice, defaulting to Human vs Computer.")
            self.player1 = Player('human', 1)
            self.player2 = Player('computer', 2)

    def start(self) -> None:
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        self.choose_game_mode()
        # Play Tic-Tac-Toe
        # load Q-table
        if 'agent' in [self.player1, self.player2]:
            self.q_agent.load_q_table()

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

    def game(self, current_turn) -> None:
        print(f'----- Player{current_turn.get_player_number} : {current_turn.get_player} turn -----')
        self.board.print_board()
        state = str(self.board.game_board)

        while True:  # Round
            print(f'----- Player{current_turn.get_player_number} : {current_turn.get_player} turn -----')
            if current_turn.get_player == 'human':
                move = current_turn.get_human_move()
            elif current_turn.get_player == 'agent':
                # agent
                available_actions = self.board.get_possible_moves()
                move = self.q_agent.choose_action(state, available_actions)
            else:
                # computer
                move = current_turn.get_computer_move(self.board)

            self.board.submit_move(current_turn, Move(move))
            self.board.print_board()

            if self.board.check_is_game_over(current_turn, Move(move)):
                print(f"Awesome. Player{current_turn.get_player_number} : {current_turn.get_player} won the game!")
                break
            elif self.board.check_is_tie():
                print("It's a tie! Try again!")
                break

            # Switch turns
            current_turn = self.player2 if current_turn == self.player1 else self.player1

    @staticmethod
    def start_new_round(board) -> None:
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()

    def train_agent(self, num_episodes: int, reset_q_table: bool = True) -> list:
        """
        Automatically train the Q-learning agent with a specified number of episodes.

        Parameters:
            num_episodes (int): episode length
            reset_q_table (bool): If True, starts training with a fresh Q-table.
                                  If False, loads an existing Q-table before training.

        Return:
            list: A list of cumulative rewards per episode
        """

        print("Training the agent")
        self.player1 = Player('agent', 1)
        self.player2 = Player('computer', 2)

        # Load existing Q-table
        if not reset_q_table:
            self.q_agent.load_q_table()

        wins, losses, ties = 0, 0, 0  # Track performance metrics
        episode_rewards = [0] * num_episodes  # Pre-allocate rewards list

        for episode in range(num_episodes):
            self.board.reset_board()  # Reset the board at the start of each episode
            state = str(self.board.game_board)
            current_turn = self.player1 if random.choice([True, False]) else self.player2
            cumulative_reward = 0

            while True:
                available_actions = self.board.get_possible_moves()

                # Agent or Computer chooses an action
                if current_turn.get_player == 'agent':
                    move = self.q_agent.choose_action(state, available_actions)
                else:
                    move = current_turn.get_computer_move(self.board)

                self.board.submit_move(current_turn, Move(move))  # Make the move
                next_state = str(self.board.game_board)  # Get the new board state

                # Check game outcome and update Q-values
                if self.board.check_is_game_over(current_turn, Move(move)):
                    reward = self.WIN if current_turn.get_player == 'agent' else self.LOSE
                    self.q_agent.update_q_value(state, move, next_state, reward)
                    cumulative_reward += reward
                    if reward == self.WIN:
                        wins += 1
                    else:
                        losses += 1
                    break
                elif self.board.check_is_tie():
                    reward = self.TIE  # Neutral reward for tie
                    self.q_agent.update_q_value(state, move, next_state, reward)
                    cumulative_reward += reward
                    ties += 1
                    break
                else:
                    # For non-terminal state, reward is 0
                    reward = 0
                    self.q_agent.update_q_value(state, move, next_state, reward)
                    cumulative_reward += reward
                    state = next_state  # Transition to the next state

                # Switch turns
                current_turn = self.player2 if current_turn == self.player1 else self.player1

            episode_rewards[episode] = cumulative_reward
            # Print progress every 1000 episodes
            if (episode + 1) % 1000 == 0:
                avg_reward = sum(episode_rewards[-1000:]) / 1000  # Average reward for last 1000 episodes
                print(f"Training progress: Episode {episode + 1}/{num_episodes}, Avg Reward (last 1000): {avg_reward:.2f}")

            # Decay exploration rate to focus on exploitation over time
            self.q_agent.decay_epsilon()
        return episode_rewards

    def save_training_data(self, episode_rewards: list, filename: str) -> None:
        """Save episode rewards and game results to CSV files for analysis."""
        episode_len = len(episode_rewards)
        game_results = ['win'] * episode_len
        for i in range(0, episode_len):
            if episode_rewards[i] == self.LOSE:
                game_results[i] = 'lose'
            elif episode_rewards[i] == self.TIE:
                game_results[i] = 'tie'

        training_result_df = pd.DataFrame({"Episode": range(len(episode_rewards)),
                                           "Reward": episode_rewards, "Result": game_results})
        training_result_df.to_csv(filename, index=False)
        print("Training data saved.")
