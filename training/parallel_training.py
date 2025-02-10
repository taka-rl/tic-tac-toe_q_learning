import multiprocessing
from config import CONFIGURATIONS
from training import train_q_agent
import time


if __name__ == "__main__":
    num_processes = min(len(CONFIGURATIONS), multiprocessing.cpu_count())
    print(f"The number of processors to be used: {num_processes}")

    start_time = time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.map(train_q_agent, CONFIGURATIONS)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Total training time: {elapsed_time:.2f} seconds')
