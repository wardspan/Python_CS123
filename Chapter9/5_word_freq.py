# Write a program that asks the users for a text file. The program should create a 
# dictionary in which the keys are the individual words found in the file and the 
# values are the number of times each word appears. For example, if the word “the” appears 128 times, 
# the dictionary would contain an element with 'the' as the key and 128 as the value. 
# The program should either display the frequency of each word or create a second file containing a 
# list of each word and its frequency.


def main():
    # Ask the user for the text file path
    file_path = input("Enter the path of the text file: ")

    # Create an empty dictionary to store word frequencies
    word_freq = {}

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.split()
            # Iterate over each word
            for word in words:
                # Remove any punctuation marks from the word
                word = word.strip(".,!?")
                # Convert the word to lowercase
                word = word.lower()
                # Check if the word is already in the dictionary
                if word in word_freq:
                    # If it is, increment the frequency by 1
                    word_freq[word] += 1
                else:
                    # If it is not, add the word to the dictionary with a frequency of 1
                    word_freq[word] = 1

    # Display the frequency of each word
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

    # Alternatively, create a second file containing a list of each word and its frequency
    output_file_path = input("Enter the path of the output file: ")
    with open(output_file_path, 'w') as output_file:
        for word, freq in word_freq.items():
            output_file.write(f"{word}: {freq}\n")
            
if __name__ == "__main__":
    main()