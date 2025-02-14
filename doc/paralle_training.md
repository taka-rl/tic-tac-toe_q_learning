# Parallel Training

## Tips
You can see how many cores you can use for the parallel training  
```
multiprocessing.cpu_count()
```

Parallel training is executed in the following code
```
with multiprocessing.Pool(processes=num_processes) as pool:
  pool.map(train_q_agent, CONFIGURATIONS)
```
## Training speed 
The training speed check was done with the following conditions.  
- Conditions: 100000 episodes × 20 sets  
  - Non-parallel: 579.29 sec  
  - Parallel: 172.47 sec (8 cores were used.)

  
