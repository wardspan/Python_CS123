# Write a program with a function that accepts a string as an argument and 
# returns the number of vowels that the string contains. The application 
# should have another functionthat accepts a string as an argument and 
# returns the number of consonants that the string contains. The application 
# should let the user enter a string, and should display the number of vowels 
# and the number of consonants it contains.

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def count_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count

def main():
    user_input = input("Enter a string: ")
    vowel_count = count_vowels(user_input)
    consonant_count = count_consonants(user_input)

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    
if __name__ == "__main__":
    main()