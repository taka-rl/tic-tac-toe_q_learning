from src.game import TicTacToeGame
from config import CONFIGURATIONS
import time


def train_q_agent(config):
    """Train the Q-learning agent"""
    print(f"Starting training with configuration: {config.identifier}")
    game = TicTacToeGame(
        learning_rate=config.learning_rate,
        discount_factor=config.discount_factor,
        epsilon=config.epsilon
    )

    # Training Q-learning agent
    episode_rewards = game.train_agent(num_episodes=config.num_episodes, reset_q_table=True)

    # Save Q-table and results with a unique filename based on config identifier
    game.q_agent.save_q_table(f"../training/{config.identifier}_q_table.csv")
    game.save_training_data(episode_rewards=episode_rewards,
                            filename=f"../training/{config.identifier}_results.csv")
    print(f"Completed training with configuration: {config.identifier}\n")


if __name__ == "__main__":

    start_time = time.time()
    for conf in CONFIGURATIONS:
        train_q_agent(conf)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Total training time: {elapsed_time} seconds')
