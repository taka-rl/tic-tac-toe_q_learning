"""
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
