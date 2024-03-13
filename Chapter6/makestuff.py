import random

# Generate a list of random integers
numbers = [random.randint(1, 100) for _ in range(25)]

# Save the numbers to a file
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")