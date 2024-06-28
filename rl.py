"""
Future work:
・Introduce Q-learning algorithm
https://chat.openai.com/share/6075678c-eb0d-4420-87cb-81bdd79841ac
https://medium.com/@ardra4/tic-tac-toe-using-q-learning-a-reinforcement-learning-approach-d606cfdd64a3
https://medium.com/@kaneel.senevirathne/teaching-agents-to-play-tic-tac-toe-using-reinforcement-learning-7a9d4d6ee9b3
https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial?dc_referrer=https%3A%2F%2Fwww.google.com%2F
https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542

・Training will be done automatically.
・count win/lose/draw in the training
・store state value properly in computer or player tern
・calculate q-learning table properly
・ask to input a number again if the number has been already occupied

"""

import random
from player import Player
from board import Board
from move import Move


NUM_EPISODES = 10000


class QLearningAgent:
    """
    Q-learning equation:

    Steps in Q-Learning Algorithm:
        1: Initialize the Q-values for all state-action pairs arbitrarily (often to zero).
        2: Observe the current state
        3: Select an action a based on the current policy (e.g., ε-greedy).
        4: Perform the action a and observe the reward r and the next state
        5: Update the Q-value using the Q-learning equation.
        6: Set the current state s to the next state
        7: Repeat steps 3-6 until the termination condition is met.

    Q values are updated by the following equation:
        Q_new(s,a) = (1 - α) * Q(s,a) + α * (r + γ * max(Q(s_dash,a_dash)) - Q(s,a))

        State s: The current configuration of the board.
        Action a: Placing a marker on an empty cell.
        Reward r: +1 for a win, -1 for a loss, 0 for a draw.


    Q table:



    Action/state/reward:
    """

    def __init__(self, epsilon=0.1, alpha=0.1, gamma=0.9):
        self.q_values = {}  # Q-values dictionary
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.q_player = Player(False)

    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, value):
        current_q = self.get_q_value(state, action)
        new_q = (1 - self.alpha) * current_q + self.alpha * value
        self.q_values[(state, action)] = new_q

    def choose_action(self, state, possible_actions):
        if random.random() < self.epsilon:
            move = Move(int(random.choice(possible_actions)))
            return move  # Exploration
        else:
            max_q_value = max(self.get_q_value(state, action) for action in possible_actions)
            best_actions = [action for action in possible_actions if self.get_q_value(state, action) == max_q_value]
            move = Move(int(random.choice(best_actions)))
            return move  # Exploitation

    def train(self, state, action, reward, next_state):
        max_next_q = max(self.get_q_value(next_state, next_action) for next_action in range(9))
        target = reward + self.gamma * max_next_q
        self.update_q_value(state, action, target)


class RLGame:
    def __init__(self):
        self.q_agent = QLearningAgent()
        self.board = Board()
        self.player = Player()
        self.computer = Player(False)

    def state_to_tuple(self):
        return self.board.get_state(self.q_agent)

    def reward(self, player, move):
        if self.board.check_is_game_over(player, move):
            if player == self.q_agent.q_player:
                print()
                return 1
            elif player == self.player:
                return -1
            elif player == self.computer:
                return -1
        elif self.board.check_is_tie():
            return 0.5
        else:
            return 0

    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        self.board.print_board()

        while True:  # Game loop
            move = self.player.get_move()
            self.board.submit_move(self.player, move)
            self.board.print_board()
            reward = self.reward(self.player, move)
            if not reward == 0:
                self.q_agent.train(self.state_to_tuple(), move, reward, self.state_to_tuple())
                print("player wins!", "reward:", reward)
                break

            # Q-learning agent move
            state = self.state_to_tuple()
            possible_actions = self.board.get_possible_moves()
            action = self.q_agent.choose_action(state, possible_actions)
            self.board.submit_move(self.q_agent.q_player, action)
            self.board.print_board()
            next_state = self.state_to_tuple()

            reward = self.reward(self.q_agent.q_player, action)
            if not reward == 0:
                self.q_agent.train(state, action, reward, next_state)
                print("agent wins!", "reward:", reward)
                break
            else:
                self.q_agent.train(state, action, reward, next_state)

    def training(self):
        win, lose, draw = 0, 0, 0
        for episode in range(NUM_EPISODES):
            while True:  # Game loop
                state = self.state_to_tuple()
                move = self.computer.get_move()
                self.board.submit_move(self.computer, move)
                next_state = self.state_to_tuple()
                # self.board.print_board()
                reward = self.reward(self.player, move)
                if not reward == 0:
                    self.q_agent.train(state, move, reward, next_state)
                    print("player wins!", "reward:", reward)
                    break
                else:
                    self.q_agent.train(state, move, reward, next_state)

                # Q-learning agent move
                state = self.state_to_tuple()
                possible_actions = self.board.get_possible_moves()
                action = self.q_agent.choose_action(state, possible_actions)
                self.board.submit_move(self.q_agent.q_player, action)
                # self.board.print_board()
                next_state = self.state_to_tuple()

                reward = self.reward(self.q_agent.q_player, action)
                if not reward == 0:
                    self.q_agent.train(state, action, reward, next_state)
                    print("agent wins!", "reward:", reward)
                    break
                else:
                    self.q_agent.train(state, action, reward, next_state)

            # reset the board
            self.board.reset_board()

        # show the result
        print("--------------- training result ---------------")
        print()
        print()


if __name__ == "__main__":
    game = RLGame()
    # train the agent
    game.training()
    # play against the player
    game.start()

    print(game.q_agent.q_values)
