import random
import csv


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
        Reward r: +1 for a win, -1 for a loss, 0.5 for a draw.

    Action: Choose a move between 1 and 9
    State: board information
    Reward:
        win: +1 reward
        tie: 0.5 reward
        lose: -1 reward

    Q table: stored as a csv file
        state, action, q_value
            "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]",1,0.0

    Links:
        ・Introduce Q-learning algorithm
        https://chat.openai.com/share/6075678c-eb0d-4420-87cb-81bdd79841ac
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

    def get_q_value(self, state, action):
        """Get the Q-value for a given state-action pair, initializing to 0 if not present."""
        if state not in self.q_table:
            self.q_table[state] = {}
        return self.q_table[state].get(action, 0.0)

    def update_q_value(self, state, action, next_state, reward):
        """Update the Q-value for a state-action pair using the Q-learning update rule."""
        current_q = self.get_q_value(state, action)
        future_q_values = [self.get_q_value(next_state, next_action) for next_action in
                           self.q_table.get(next_state, {})]
        max_future_q = max(future_q_values) if future_q_values else 0

        # Q-learning formula
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[state][action] = new_q

    def choose_action(self, state, available_actions):
        """Choose an action based on epsilon-greedy policy."""
        if random.uniform(0, 1) < self.epsilon:  # Explore with probability epsilon
            return random.choice(available_actions)

        # Exploit: choose action with highest Q-value
        q_values = {action: self.get_q_value(state, action) for action in available_actions}
        max_q = max(q_values.values())

        # Break ties randomly
        best_actions = [action for action, q in q_values.items() if q == max_q]
        return random.choice(best_actions)

    def decay_epsilon(self, decay_rate=0.99):
        """Decay epsilon to reduce exploration over time."""
        self.epsilon *= decay_rate

    def save_q_table(self, filename="./training/q_table.csv"):
        """Save Q-table to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["state", "action", "q_value"])
            for state, actions in self.q_table.items():
                for action, q_value in actions.items():
                    writer.writerow([state, action, q_value])
            print("Saved Q-table")

    def load_q_table(self, filename="./training/q_table.csv"):
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
