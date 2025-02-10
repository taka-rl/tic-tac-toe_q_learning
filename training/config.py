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
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_10"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_11"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_12"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_13"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_14"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_15"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_16"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_17"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_18"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_19"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_20"),
]
