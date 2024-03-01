# write a program that will flip a simultaneous flips 1000000000 coins 
# in parallel. The program should report the number of heads and tails 
# that were flipped and compute the percentage of heads and tails. 
# The program will also keep track of how long it took to flip the coin 
# and display the time in seconds.


import multiprocessing
import time
import random

def flip_coin(num_flips):
    heads = 0
    tails = 0

    for _ in range(num_flips):
        if random.choice([True, False]):
            heads += 1
        else:
            tails += 1

    return heads, tails

if __name__ == '__main__':
    num_coins = 1000000000

    start_time = time.time()

    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    results = pool.map(flip_coin, [num_coins // num_processes] * num_processes)

    pool.close()
    pool.join()

    total_heads = sum(result[0] for result in results)
    total_tails = sum(result[1] for result in results)

    end_time = time.time()
    elapsed_time = end_time - start_time

    percentage_heads = (total_heads / num_coins) * 100
    percentage_tails = (total_tails / num_coins) * 100

    print(f"Number of Processes: {num_processes}")
    print(f"Number of heads: {total_heads}")
    print(f"Number of tails: {total_tails}")
    print(f"Percentage of heads: {percentage_heads}%")
    print(f"Percentage of tails: {percentage_tails}%")
    print(f"Elapsed time: {elapsed_time} seconds")