class Config:
    def __init__(self, learning_rate, discount_factor, epsilon, num_episodes, identifier):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.num_episodes = num_episodes
        self.identifier = identifier  # Unique identifier for saving files


CONFIGURATIONS = [
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_1"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_2"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_3"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_4"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_5"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_6"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_7"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_8"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_9"),
]
