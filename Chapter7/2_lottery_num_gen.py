import random

# Design a program that generates a seven-digit lottery number. 
# The program should gener- ate seven random numbers, each in the range of 0 through 9, 
# and assign each number to a list element. Then write another loop that displays the contents of the list.

def main():
    # Generate seven random numbers and assign each number to a list element
    lottery_numbers = []
    for _ in range(7):
        number = random.randint(0, 9)
        lottery_numbers.append(number)

    # Display the contents of the list
    for number in lottery_numbers:
        print(number)

if __name__ == '__main__':
    main()
    
