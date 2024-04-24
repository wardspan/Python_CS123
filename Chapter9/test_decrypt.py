def decrypt_file(filename, cipher_dict):
    """Decrypts a file using the provided cipher dictionary.

    Args:
        filename (str): The path to the encrypted file.
        cipher_dict (dict): The dictionary mapping original characters to encrypted characters.
    """

    # Construct the reverse lookup for decryption
    decryption_dict = {value: key for key, value in cipher_dict.items()}

    with open(filename, 'r') as encrypted_file:
        encrypted_text = encrypted_file.read()

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += decryption_dict.get(char, char)  # Decrypt or leave unchanged if unknown

    print(decrypted_text)

# Main execution
if __name__ == "__main__":
    cipher_dict = {
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
    ' ': ' '
    }

    filename = input("Enter the name of the encrypted file: ")
    decrypt_file(filename, cipher_dict) 
