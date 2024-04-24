# Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:
# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
# The program should ask the user for a specified text file, read its contents, 
# then use the dictionary to write an encrypted version of the file’s contents to a second file.
# Each character in the second file should contain the code for the corresponding character in the first file.

# Define the codes dictionary
codes = {
    'A': '%', 'a': '9',
    'B': '@', 'b': '#',
    'C': '!', 'c': '8',
    'D': '$', 'd': '7',
    'E': '^', 'e': '6',
    'F': '&', 'f': '5',
    'G': '*', 'g': '4',
    'H': '(', 'h': '3',
    'I': ')', 'i': '2',
    'J': '-', 'j': '1',
    'K': '_', 'k': '0',
    'L': '+', 'l': '=',
    'M': '[', 'm': ']',
    'N': '{', 'n': '}',
    'O': ':', 'o': ';',
    'P': '"', 'p': "'",
    'Q': '<', 'q': '>',
    'R': ',', 'r': '.',
    'S': '?', 's': '/',
    'T': '|', 't': '\\',
    'U': '`', 'u': '~',
    'V': '!', 'v': '@',
    'W': '~', 'w': '$',
    'X': '%', 'x': '^',
    'Y': '&', 'y': '*',
    'Z': '(', 'z': ')',
    ' ': ' ',
}

def main():
    # Ask the user for the input and output file names
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")

    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read the contents of the input file
        contents = file.read()

    # Encrypt the contents using the codes dictionary
    encrypted_contents = ''
    for char in contents:
        if char in codes:
            encrypted_contents += codes[char]
        else:
            encrypted_contents += char

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Write the encrypted contents to the output file
        file.write(encrypted_contents)

    print("File encrypted successfully!")
    
if __name__ == "__main__":
    main()
    