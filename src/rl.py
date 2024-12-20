import random
import csv


class QLearningAgent:
    """
    Q-learning algorithm:
        Q-learning is a model-free, value-based, off-policy reinforcement learning (RL) algorithm
        based on the Bellman equation. It uses a Q-table to store Q-values for state-action pairs,
        which represent the expected future rewards for taking specific actions in specific states.

    Steps in Q-Learning Algorithm:
        1: Initialize the Q-values for all state-action pairs arbitrarily (often to zero).
        2: Observe the current state
        3: Select an action a based on the current policy (e.g., ε-greedy).
        4: Perform the action a and observe the reward r and the next state
        5: Update the Q-value using the Q-learning equation.
        6: Set the current state s to the next state
        7: Repeat steps 2-6 until the termination condition is met.

    Q-table:
        The Q-table is defined as a list data type and is stored as a csv file with the following format.
        state, action, q_value
            "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]", 1, 0.0

    Q-value Update Equation:
        The Q-values are updated using the standard Q-learning update equation:
            Q_new(s, a) = Q(s, a) + alpha * (r + γ * max(Q(s', a')) - Q(s, a))
        Where:
            - Q(s, a): Current Q-value for the state-action pair (s, a)
            - alpha: Learning rate
            - γ: Discount factor (gamma)
            - max(Q(s', a')): Maximum Q-value for the next state s'
            - s: Current state
            - a: Action taken in the current state
            - r: Reward received after taking action a
        Reward values:
            - Win: +1
            - Tie: +0.5
            - Loss: -1

    Reinforcement Learning (RL) Environment:
        - Action: Choose a move between 1 and 9.
        - State: Board configuration represented as a string, e.g., "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]".
        - Reward:
            - Win: +1
            - Tie: +0.5
            - Loss: -1

    Links:
        ・Introduce Q-learning algorithm
        https://towardsdatascience.com/an-ai-agent-learns-to-play-tic-tac-toe-part-3-training-a-q-learning-rl-agent-2871cef2faf0
        https://medium.com/@ardra4/tic-tac-toe-using-q-learning-a-reinforcement-learning-approach-d606cfdd64a3
        https://medium.com/@kaneel.senevirathne/teaching-agents-to-play-tic-tac-toe-using-reinforcement-learning-7a9d4d6ee9b3
        https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial?dc_referrer=https%3A%2F%2Fwww.google.com%2F
        https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542

    """

    def __init__(self, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.q_table = {}  # Initialize empty Q-table
        self.alpha = learning_rate  # Learning rate
        self.gamma = discount_factor  # Discount factor
        self.epsilon = epsilon  # Exploration rate

    def get_q_value(self, state, action) -> dict:
        """Get the Q-value for a given state-action pair, initializing to 0 if not present."""
        if state not in self.q_table:
            self.q_table[state] = {}
        return self.q_table[state].get(action, 0.0)

    def update_q_value(self, state, action, next_state, reward) -> None:
        """Update the Q-value for a state-action pair using the Q-learning update rule."""
        current_q = self.get_q_value(state, action)
        future_q_values = [self.get_q_value(next_state, next_action) for next_action in
                           self.q_table.get(next_state, {})]
        max_future_q = max(future_q_values) if future_q_values else 0

        # Q-learning formula
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[state][action] = new_q

    def choose_action(self, state, available_actions) -> int:
        """Choose an action based on epsilon-greedy policy."""
        if random.uniform(0, 1) < self.epsilon:  # Explore with probability epsilon
            return random.choice(available_actions)

        # Exploit: choose action with highest Q-value
        q_values = {action: self.get_q_value(state, action) for action in available_actions}
        max_q = max(q_values.values())

        # Break ties randomly
        best_actions = [action for action, q in q_values.items() if q == max_q]
        return random.choice(best_actions)

    def decay_epsilon(self, decay_rate=0.99) -> None:
        """Decay epsilon to reduce exploration over time."""
        self.epsilon *= decay_rate

    def save_q_table(self, filename):
        """Save Q-table to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["state", "action", "q_value"])
            for state, actions in self.q_table.items():
                for action, q_value in actions.items():
                    writer.writerow([state, action, q_value])
            print("Saved Q-table")

    def load_q_table(self, filename="../training/q_table.csv") -> None:
        """Load Q-table from a CSV file."""
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for state, action, q_value in reader:
                    if state not in self.q_table:
                        self.q_table[state] = {}
                    self.q_table[state][int(action)] = float(q_value)
                print("Successfully load Q-table.")
        except FileNotFoundError:
            print("Q-table file not found. Starting with an empty Q-table.")
