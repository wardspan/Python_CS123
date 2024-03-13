# Assume a file containing a series of integers is named numbers.txt 
# and exists on the computer’s disk. Write a program that calculates 
# the average of all the numbers stored in the file.

# Open the file for reading
with open('/Users/wardspan/Code/Python_CS123/Chapter6/numbers.txt', 'r') as file:
    # Read all the numbers from the file
    numbers = [int(line) for line in file]

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the average
print("The average is:", average)