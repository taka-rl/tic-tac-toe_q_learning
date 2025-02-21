# Tic-tac-toe with Q-learning
This is a tic-tac-toe game built using Q-learning, a reinforcement learning (RL) algorithm.

As a result of the training with 100,000 episodes where the agent played against a computer that made random moves, the agent won at around 75% of the games against the computer. The average reward was approximately 0.7, and the maximum reward exceeded 0.9.

## About Q-learning
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
            - r: Reward received after taking action
    Links:
        ・Introduce Q-learning algorithm
        https://towardsdatascience.com/an-ai-agent-learns-to-play-tic-tac-toe-part-3-training-a-q-learning-rl-agent-2871cef2faf0
        https://medium.com/@ardra4/tic-tac-toe-using-q-learning-a-reinforcement-learning-approach-d606cfdd64a3
        https://medium.com/@kaneel.senevirathne/teaching-agents-to-play-tic-tac-toe-using-reinforcement-learning-7a9d4d6ee9b3
        https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial?dc_referrer=https%3A%2F%2Fwww.google.com%2F
        https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542

## RL Environment
Action: Choose a move between 1 and 9.  
State: Board configuration represented as a string, e.g., "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]".  
Reward: Win: +1, Tie: +0.5, Loss: -1

## Folder structure

    ├── src                     # codes for tic-tac-toe environment
    │   ├── board.py            # for board
    │   ├── game.py             # for game
    │   ├── move.py             # for move
    │   ├── player.py           # for player
    │   └── rl.py               # for Q-learning algorithm
    ├── training                # codes for training
    │   ├── training_results    # 
    │   │    └── plan1          # training plan1 result files
    │   ├── training.py         # for training
    │   ├── result_analysis.py  # for analyzing the training result
    │   ├── training_result.csv # training result file
    │   ├── q_table.csv         # Q-table file generated after 100,000 episodes
    │   └── README.md           #
    ├── main.py                 # Run the app
    ├── .gitignore
    ├── requirements.txt
    └── README.md


## Preparation to use
1. Clone this project  
``` git clone https://github.com/taka-rl/tic-tac-toe_q_learning.git``` 
2. If you would like to only play Tic-Tac-Toe, please see "Play Tic-Tac-Toe".  
3. If you would like to train the agent, Run the following command for the libraries:  
   On Windows type:
   ```python -m pip install -r requirements.txt```  
   On MacOS type:
   ```pip3 install -r requirements.txt```


## Play Tic-Tac-Toe
If you would like to play tic-tac-toe simply, run main.py.  
Choose a game mode between 1 and 6.  
![image](https://github.com/user-attachments/assets/d3f527d9-5600-40a5-b7e0-9ece4d765c8f)

## Training
If you would like to play tic-tac-toe simply, run `training.py`.   
Please refer to this [link](https://github.com/taka-rl/tic-tac-toe_q_learning/tree/main/training/README.md) for more information.


## Result
### Plan 1: Same Parameter Settings with Different Numbers of Episodes  
Training environment
- During training, the agent plays against a computer that makes random moves.
- Reward setting: win=1, tie=0.5, lose=-1
- The parameter settings are as follows in config.py:
```
CONFIGURATIONS = [
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=1000, identifier="training1_1"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=10000, identifier="training1_2"),
    Config(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, num_episodes=100000, identifier="training1_3"),
]
```
Expectation: As the number of episodes increases, the average reward is expected to increase.  
Result: The average reward increased, and the number of wins also rose.  


The average reward was calculated every 100 games.
The number of episode is 1000.  
![image](https://github.com/user-attachments/assets/929e6e52-d8cb-46b2-a3a7-43354cd9d029)

The number of episode is 10000.  
![image](https://github.com/user-attachments/assets/98de423d-3650-464b-997d-a556b017a35c)

The number of episode is 100000.  
![image](https://github.com/user-attachments/assets/857a8069-309d-4447-a4a1-bd40c267fffb)
![image](https://github.com/user-attachments/assets/068547f0-fd95-4824-991d-b64a9b122756)

Win/Lose/Tie:  
Through the training, the number of win increased, the number of lose decreased gradually.   
![image](https://github.com/user-attachments/assets/5c3700ef-904b-429e-af85-bf0a1b35ab64)

## Todo
- Conducting Multi-Agent training
