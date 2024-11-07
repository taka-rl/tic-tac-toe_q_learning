from src.game import TicTacToeGame


game = TicTacToeGame()

# Run training
game.train_agent(num_episodes=100000)
