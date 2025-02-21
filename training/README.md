## Training
### Training preparation  
1. You can set parameters for the training in config.py  
![Screenshot 2024-11-11 at 10 23 30](https://github.com/user-attachments/assets/1f6e7db7-3d50-42ce-81cc-77329ce34293)

2. When you are ready, then run `training.py`. Or if you would like to use parallel training, run `parallel_training.py`.  
3. When the training finished, the following messages show up  
![image](https://github.com/user-attachments/assets/b6cd8e47-0b38-428d-8ba9-afb9ec89295b)

4. After the training, q_table.csv and training_result.csv files are saved in the training folder.  
    q_table.csv looks like this.  
    ![image](https://github.com/user-attachments/assets/4ed68e55-4962-431f-a8e9-ac6438b9fd37)  
    training_result.csv looks like this.  
    ![image](https://github.com/user-attachments/assets/e57ead6e-f8a4-4460-bf55-ea26671b5c36)  

## How to use result_analysis.py for result analysis
1. Make sure the result file path in `result_analysis.py`
   ![image](https://github.com/user-attachments/assets/7fce67d6-558b-4423-8f5a-c8c083c7d2f3)

2. Make sure the identifier value in CONFIGURATION defined in config.py  
   The identifier values must be matched with the result files.

3. Run result_analysis.py
   You will see the figures on the Result section.  
