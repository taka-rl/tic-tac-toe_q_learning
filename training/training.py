from src.game import TicTacToeGame

# Set parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1
num_episodes = 1000

game = TicTacToeGame(learning_rate=learning_rate, discount_factor=discount_factor, epsilon=epsilon)

# Run training
game.train_agent(num_episodes=num_episodes)
