# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# It should handle any IOError exceptions that are raised when the file is 
# opened and data is read from it.
# It should handle any ValueError exceptions that are raised when the items that 
# are read from the file are converted to a number.

try:
    with open('/Users/wardspan/Code/Python_CS123/Chapter6/numbers.txt', 'r') as file:
        numbers = file.readlines()
        numbers = [int(num) for num in numbers]
        average = sum(numbers) / len(numbers)
        print("Average:", average)
except IOError:
    print("Error: Failed to open or read the file.")
except ValueError:
    print("Error: Failed to convert the items to numbers.")