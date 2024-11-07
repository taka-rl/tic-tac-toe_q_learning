import random
import matplotlib.pyplot as plt
from src.player import Player
from src.board import Board
from src.move import Move
from src.rl import QLearningAgent


class TicTacToeGame:
    def __init__(self) -> None:
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.q_agent = QLearningAgent()

    def choose_game_mode(self) -> None:
        """Prompt to choose a game mode."""
        print("Choose a game mode:")
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

    def start(self):
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

    def game(self, current_turn):
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
                move = Move(move)
            else:
                # computer
                move = current_turn.get_computer_move(self.board)

            self.board.submit_move(current_turn, move)
            self.board.print_board()

            if self.board.check_is_game_over(current_turn, move):
                print(f"Awesome. Player{current_turn.get_player_number} : {current_turn.get_player} won the game!")
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

    def train_agent(self, num_episodes):
        """Automatically train the Q-learning agent with a specified number of episodes."""
        print("Training the agent")
        self.player1 = Player('agent', 1)
        self.player2 = Player('computer', 2)

        self.q_agent.load_q_table()  # Load existing Q-table if any

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
                    reward = 1 if current_turn.get_player == 'agent' else -1  # Reward based on agent's perspective
                    self.q_agent.update_q_value(state, move, next_state, reward)
                    cumulative_reward += reward
                    if reward == 1:
                        wins += 1
                    else:
                        losses += 1
                    break
                elif self.board.check_is_tie():
                    reward = 0.5  # Neutral reward for tie
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

        # Save Q-table after training
        self.q_agent.save_q_table("q_table.csv")
        print(f"Training complete: {wins} Wins, {losses} Losses, {ties} Ties")

        # Plot reward progress if matplotlib is available
        plt.plot(range(num_episodes), episode_rewards)
        plt.xlabel("Episodes")
        plt.ylabel("Cumulative Reward")
        plt.title("Reward Progress Over Training")
        plt.show()
