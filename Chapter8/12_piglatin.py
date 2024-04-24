#Write a program that accepts a sentence as input and converts each word to “Pig Latin.” 
# In one version, to convert a word to Pig Latin, you remove the first letter and place 
# that letter at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def main():
    
    # Accept input sentence
    sentence = input("Enter a sentence: ")

    # Split the sentence into words
    words = sentence.split()

    # Convert each word to Pig Latin
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)

    # Join the Pig Latin words back into a sentence
    pig_latin_sentence = " ".join(pig_latin_words)

    # Print the Pig Latin sentence
    print("English:", sentence)
    print("Pig Latin:", pig_latin_sentence)

if __name__ == "__main__":

    main()