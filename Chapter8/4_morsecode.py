# Write a program that asks the user to enter a string, and the program will convert the string to Morse code.

# Define a dictionary to map characters to Morse code
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def main():
    # Ask the user to enter a string
    user_input = input("Enter a string: ")

    # Convert the string to Morse code
    morse_code_output = ''
    for char in user_input.upper():
        if char in morse_code:
            morse_code_output += morse_code[char] + ' '
        else:
            morse_code_output += char + ' '

    # Print the Morse code output
    print("Morse code:", morse_code_output.strip())

if __name__ == "__main__":
    main()