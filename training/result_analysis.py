import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from config import CONFIGURATIONS


'''
This script presents plots from the training result files such as XXX_q_table.csv and XXX_results.csv.

There are 2 modes, which you can set in the following code: 
    plot_mode = "combined": Combines all configurations into a single plot.
    plot_mode = "separate": Creates individual plots for each configuration.

Reward progress:
    In "combined" mode, it plots the running average rewards for all configurations on one graph.
    In "separate" mode, it generates a separate plot for each configuration, showing its reward progression over episodes.

Win/Loss/Tie distribution:
    In "combined" mode, it uses a stacked bar plot to show win/loss/tie distribution across all configurations in one plot.
    In "separate" mode, it creates individual pie plots for each configuration.

Q-values heatmap:
    For an example state, the Q-values heatmap is combined across configurations in "combined" mode.
    In "separate" mode, it generates individual heatmaps for each configuration, showing Q-values for the example state.

'''

# Set the plot mode to "combined" or "separate"
plot_mode = "separate"

# Initialize empty DataFrames to store cumulative data
q_tables = pd.DataFrame(columns=["state", "action", "q_value", "config_id"])
training_results = pd.DataFrame(columns=["Episode", "Reward", "Result", "Running_Avg_Reward", "config_id"])

# Load each Q-table and result file for each configuration
file_path = "training_results/plan1/"
for config in CONFIGURATIONS:
    config_id = config.identifier
    q_table_path = file_path + f"{config_id}_q_table.csv"
    training_result_path = file_path + f"{config_id}_results.csv"

    # Load Q-table and add a column to indicate the configuration ID
    q_table_df = pd.read_csv(q_table_path)
    q_table_df["config_id"] = config_id
    q_tables = pd.concat([q_tables, q_table_df], ignore_index=True)

    # Load training results and add a column to indicate the configuration ID
    training_result_df = pd.read_csv(training_result_path)
    training_result_df["config_id"] = config_id
    training_result_df["Running_Avg_Reward"] = training_result_df["Reward"].rolling(window=100).mean()
    training_results = pd.concat([training_results, training_result_df], ignore_index=True)

# Q-table Analysis: Find the highest Q-values per state across configurations
highest_q_values = q_tables.groupby(["state", "config_id"])["q_value"].max()
print("Highest Q-values per state by configuration:")
print(highest_q_values)

# Reward Tracking: Calculate running averages of rewards for each configuration
print("Running Average of Rewards (last 100 episodes) per configuration:")
for config_id in training_results["config_id"].unique():
    print(f"\nConfiguration {config_id}")
    config_data = training_results[training_results["config_id"] == config_id]
    print(config_data[["Episode", "Running_Avg_Reward"]].tail(10))  # Last 10 episodes for each config

# Game Results Summary by Configuration
print("\nGame Results Summary by Configuration:")
game_summary = training_results.groupby("config_id")["Result"].value_counts()
print(game_summary)

# Plot Reward Progress
if plot_mode == "combined":
    plt.figure(figsize=(10, 5))
    for config_id in training_results["config_id"].unique():
        config_data = training_results[training_results["config_id"] == config_id]
        plt.plot(config_data["Episode"], config_data["Running_Avg_Reward"], label=f"Config {config_id}")

    plt.xlabel("Episode")
    plt.ylabel("Running Avg Reward (100 episodes)")
    plt.title("Reward Progress Over Training for Each Configuration")
    plt.legend()
else:  # Separate plots
    for config_id in training_results["config_id"].unique():
        config_data = training_results[training_results["config_id"] == config_id]
        plt.figure(figsize=(10, 5))
        plt.plot(config_data["Episode"], config_data["Running_Avg_Reward"], label=f"Config {config_id}")
        plt.xlabel("Episode")
        plt.ylabel("Running Avg Reward (100 episodes)")
        plt.title(f"Reward Progress Over Training - Configuration {config_id}")
        plt.legend()


# Plot Win/Lose/Tie Distribution using Bar charts
if plot_mode == "combined":
    plt.figure(figsize=(12, 6))
    game_summary.unstack().plot(kind="bar", stacked=True)
    plt.title("Win/Lose/Tie Distribution by Configuration")
    plt.xlabel("Configuration")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
else:  # Separate plots using Pie charts
    for config_id in training_results["config_id"].unique():
        config_summary = game_summary[config_id]
        # plt.figure(figsize=(8, 5))
        # config_summary.plot(kind="bar", color=["green", "red", "gray"])
        # plt.title(f"Win/Loss/Tie Distribution - Configuration {config_id}")
        # plt.xlabel("Game Outcome")
        # plt.ylabel("Frequency")

        # Pie charts
        plt.figure(figsize=(6, 6))
        plt.pie(config_summary, labels=config_summary.index, autopct="%1.1f%%", startangle=140,
                colors=["green", "red", "gray"])
        plt.title(f"Win/Lose/Tie Distribution - Configuration {config_id}")


# Q-values Heatmap for a specific example state
example_state = "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]"
example_state_q_values = q_tables[q_tables["state"] == example_state]
if not example_state_q_values.empty:
    if plot_mode == "combined":
        example_state_q_values_pivot = example_state_q_values.pivot_table(index="action", columns="config_id",
                                                                          values="q_value")
        plt.figure(figsize=(10, 8))
        sns.heatmap(example_state_q_values_pivot, annot=True, cmap="coolwarm")
        plt.title("Q-values Heatmap for Example State Across Configurations")
    else:  # Separate heatmaps
        for config_id in example_state_q_values["config_id"].unique():
            config_data = example_state_q_values[example_state_q_values["config_id"] == config_id]
            config_data_pivot = config_data.pivot_table(index="action", columns="state", values="q_value")
            plt.figure(figsize=(8, 6))
            sns.heatmap(config_data_pivot, annot=True, cmap="coolwarm")
            plt.title(f"Q-values Heatmap - Example State, Config {config_id}")

# Plot
plt.show()
