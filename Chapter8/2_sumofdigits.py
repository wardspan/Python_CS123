# Write a program that asks the user to enter a series of single-digit numbers 
# with nothing separating them. The program should display the sum of all the 
# single digit numbers in the string. For example, if the user enters 2514, 
# the method should return 12, which is the sum of 2, 5, 1, and 4.

def main():
    # Ask the user to enter a series of single-digit numbers
    numbers = input("Enter a series of single-digit numbers with no spaces between them (e.g. 2514): ")

    # Initialize the sum variable
    sum_of_digits = 0

    # Iterate over each character in the input string
    for digit in numbers:
        # Convert the character to an integer and add it to the sum
        sum_of_digits += int(digit)

    # Display the sum of the single-digit numbers
    print("The sum of the single-digit numbers is:", sum_of_digits)

if __name__ == "__main__":
    main()