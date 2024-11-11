from src.game import TicTacToeGame
from config import CONFIGURATIONS


for config in CONFIGURATIONS:
    print(f"Starting training with configuration: {config.identifier}")
    game = TicTacToeGame(
        learning_rate=config.learning_rate,
        discount_factor=config.discount_factor,
        epsilon=config.epsilon
    )
    episode_rewards = game.train_agent(num_episodes=config.num_episodes)

    # Save Q-table and results with a unique filename based on config identifier
    game.q_agent.save_q_table(f"../training/{config.identifier}_q_table.csv")
    game.save_training_data(episode_rewards=episode_rewards, filename=f"../training/{config.identifier}_results.csv")
    print(f"Completed training with configuration: {config.identifier}\n")
