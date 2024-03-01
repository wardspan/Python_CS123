# write a program that will flip a simultaneous flips 1000000000 coins
# in parallel. The program should report the number of heads and 
# tails that were flipped and compute the percentage of heads and tails. 
# The program will also keep track of how long it took to flip the 
# coin and display the time in seconds.

import multiprocessing
import random
import time

def flip_coins(num_coins):
    results = [random.choice(['Heads', 'Tails']) for _ in range(num_coins)]
    return results


if __name__ == "__main__":
    num_coins = 1000000000
    num_processes = multiprocessing.cpu_count()  # Get the number of CPU cores
    chunk_size = num_coins // num_processes
    
    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(flip_coins, [chunk_size] * num_processes)

    # Flatten the list of results
    all_results = [result for sublist in results for result in sublist]

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Counting heads and tails
    num_heads = all_results.count('Heads')
    num_tails = all_results.count('Tails')

    print(f"Number of Processes: {num_processes}")
    print(f"Number of Heads: {num_heads}")
    print(f"Number of Tails: {num_tails}")
    print(f"Percentage of Heads: {(num_heads / num_coins) * 100:.2f}%")
    print(f"Number of Tails: {(num_tails / num_coins) * 100:.2f}%")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
