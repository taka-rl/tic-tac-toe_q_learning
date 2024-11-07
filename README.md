# Tic-tac-toe with Q-learning
Under development
- need to update codes for updating q-table and q-values

## Folder structure

    ├── src                     # codes for tic-tac-toe environment
    │   ├── board.py            # for board
    │   ├── game.py             # for game
    │   ├── move.py             # for move
    │   ├── player.py           # for player
    │   └── rl.py               # for Q-learning algorithm
    ├── training                # codes for training
    │   ├── training.py         # for training
    │   ├── result_analysis.py  # for analyzing the training result
    │   ├── training_result.csv # training result file
    │   └── q_table.csv         # Q-table file
    ├── main.py                 # Run the app
    ├── .gitignore
    ├── requirements.txt
    └── README.md


## Preparation to use
1. Clone this project  
``` git clone https://github.com/taka-rl/tic-tac-toe_q_learning.git``` 

2. Choose the next step: 
## Play Tic-Tac-Toe
If you would like to play tic-tac-toe simply, run main.py.  
Choose a game mode between 1 and 6.  
![image](https://github.com/user-attachments/assets/d3f527d9-5600-40a5-b7e0-9ece4d765c8f)

## Training
If you would like to train the q-learning agent, run training.py  
You can set the number of episodes by changing num_episodes.  
![image](https://github.com/user-attachments/assets/78396e65-089b-42f5-87ea-908cad0082de)  

After the training, q_table.csv and training_result.csv files are saved in the training folder.  
q_table.csv looks like this.  
![image](https://github.com/user-attachments/assets/4ed68e55-4962-431f-a8e9-ac6438b9fd37)  
training_result.csv looks like this.  
![image](https://github.com/user-attachments/assets/e57ead6e-f8a4-4460-bf55-ea26671b5c36)  


## Result

