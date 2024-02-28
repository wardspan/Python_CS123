# write a program that will flip a coin based on how many times the user inputs and display the results.
# The program should report the number of heads and tails that were flipped and compute the percentage of heads and tails.
# The program will also keep track of how long it took to flip the coin and display the time in seconds.

import random
import time

def flip_coin(num_flips):
    heads = 0
    tails = 0

    start_time = time.time()

    for _ in range(num_flips):
        if random.choice([True, False]):
            heads += 1
        else:
            tails += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Number of flips: {num_flips}")
    print(f"Number of heads: {heads}")
    print(f"Number of tails: {tails}")
    print(f"Percentage of heads: {(heads / num_flips) * 100:.2f}%")
    print(f"Percentage of tails: {(tails / num_flips) * 100:.2f}%")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

num_flips = int(input("Enter the number of times to flip the coin: "))
flip_coin(num_flips)