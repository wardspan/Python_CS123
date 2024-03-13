# Assume a file containing a series of integers is named numbers.txt 
# and exists on the computer’s disk. Write a program that reads all 
# of the numbers stored in the file and calculates their total.

# Open the file for reading
file_path = '/Users/wardspan/Code/Python_CS123/Chapter6/numbers.txt'
with open(file_path, 'r') as file:
    # Read all the lines from the file
    lines = file.readlines()

    # Initialize the total variable
    total = 0

    # Iterate over each line and convert the numbers to integers
    for line in lines:
        # Remove any leading or trailing whitespace
        line = line.strip()
        # Convert the line to an integer and add it to the total
        total += int(line)

    # Print the total
    print("The total is:", total)