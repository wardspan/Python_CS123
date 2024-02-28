# Write a program that will generate 100 random numbers between 1 and 100. As it generates each number
# it should display the number and then indicate whether it is odd or even. At the end it should print the
# count of odd numbers and the count of even numbers. Additionally the program should print the count of numbers that were generated 
# more than once and put them in descending order.

import random

numbers = []
odd_count = 0
even_count = 0
number_counts = {}

for _ in range(100):
    number = random.randint(1, 100)
    numbers.append(number)
    if number % 2 == 0:
        print(f"{number} is even")
        even_count += 1
    else:
        print(f"{number} is odd")
        odd_count += 1

    if number in number_counts:
        number_counts[number] += 1
    else:
        number_counts[number] = 1

print(f"Count of odd numbers: {odd_count}")
print(f"Count of even numbers: {even_count}")

for number, count in number_counts.items():
    if count > 1:
        print(f"{number} has been generated {count} times before")
    else:
        print(f"{number} has been generated once")
