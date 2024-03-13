# Assume a file containing a series of names (as strings) is named names.txt 
# and exists on the computer’s disk. Write a program that displays the number 
# of names that are stored in the file. (Hint: Open the file and read every 
# string stored in it. Use a variable to keep a count of the number of 
# items that are read from the file.)

# Open the file
file_path = "/Users/wardspan/Code/Python_CS123/Chapter6/names.txt"
file = open(file_path, "r")

# Initialize a counter variable
count = 0

# Read every string stored in the file
for line in file:
    # Increment the counter for each name
    count += 1

# Close the file
file.close()

# Display the number of names
print("Number of names:", count)