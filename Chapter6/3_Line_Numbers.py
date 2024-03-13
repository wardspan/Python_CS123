# Write a program that asks the user for the name of a file. The program 
# should display the contents of the file with each line preceded
# with a line number followed by a colon. The line numbering should start at 1.

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"{i}: {line.strip()}")
except FileNotFoundError:
    print("File not found.")