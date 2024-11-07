import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 2: Load Data and Analyze with Pandas

# Load the Q-table, rewards, and results data
q_table_df = pd.read_csv("q_table.csv")
training_result_df = pd.read_csv("training_result.csv")

# Q-table Analysis
# Find the highest Q-values per state
highest_q_values = q_table_df.groupby("state")["q_value"].max()
print("Highest Q-values per state:")
print(highest_q_values)

# Reward Tracking: Calculate running average of rewards
training_result_df["Running_Avg_Reward"] = training_result_df["Reward"].rolling(window=100).mean()
print("Running Average of Rewards (last 100 episodes):")
print(training_result_df.tail(10))  # Display last 10 episodes for reference

# Game Results Summary
game_summary = training_result_df["Result"].value_counts()
print("Game Results Summary:")
print(game_summary)


# Step 3: Visualize with Matplotlib

# Plot cumulative reward
plt.figure(figsize=(10, 5))
plt.plot(training_result_df["Episode"], training_result_df["Reward"], label="Reward per Episode", linewidth=0.5)
plt.plot(training_result_df["Episode"], training_result_df["Running_Avg_Reward"],
         label="Running Avg Reward (100 episodes)", linestyle="--")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Reward Progress Over Training")
plt.legend()

# Plot win/loss/tie distribution
plt.figure(figsize=(8, 5))
game_summary.plot(kind="bar", color=["green", "red", "gray"])
plt.title("Win/Loss/Tie Distribution")
plt.xlabel("Game Outcome")
plt.ylabel("Frequency")

# Q-values Heatmap for a specific example state
example_state_q_values = q_table_df[q_table_df["state"] == "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]"]
if not example_state_q_values.empty:
    # Use pivot_table instead of pivot
    example_state_q_values_pivot = example_state_q_values.pivot_table(index="action", columns="state", values="q_value")

    plt.figure(figsize=(8, 6))
    sns.heatmap(example_state_q_values_pivot, annot=True, cmap="coolwarm")
    plt.title("Q-values Heatmap for Example State")

# Show all figures at once
plt.show()
