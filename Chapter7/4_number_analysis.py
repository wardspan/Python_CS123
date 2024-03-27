# Design a program that asks the user to enter a series of 20 numbers. The program should store
# the numbers in a list then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list

def main():
    numbers = []
    for _ in range(20):
        number = float(input("Enter a number: "))
        numbers.append(number)
    
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    print("Numbers entered:", numbers)
    print("Lowest number:", lowest)
    print("Highest number:", highest)
    print("Total:", total)
    print("Average:", average)
    
if __name__ == '__main__':
    main()
    