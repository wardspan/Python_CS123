# Write code that does the following: opens the number_list.txt file that was created 
# by the code you wrote in question 3, reads all of the numbers from the file and 
# displays them, then closes the file.

file_path = "/Users/wardspan/Code/Python_CS123/Chapter6/number_list.txt"

with open(file_path, "r") as file:
    numbers = file.read()
    print(numbers)
    file.close()
    