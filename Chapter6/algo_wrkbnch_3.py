# Write code that does the following: opens an output file with the filename number_ list.txt
# uses a loop to write the numbers 1 through 100 to the file, then closes the file

filename = "/Users/wardspan/Code/Python_CS123/Chapter6/number_list.txt"

with open(filename, "w") as file:
    for number in range(1, 101):
        file.write(str(number) + "\n")