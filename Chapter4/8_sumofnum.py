# Write a program with a loop that asks the user to enter a series of positive numbers. 
# The user should enter a negative number to signal the end of the series. After 
# all the positive numbers have been entered, the program should display their sum.

numbers = []
while True:
    num = float(input("Enter a positive number (or a negative number to exit): "))
    if num < 0:
        break
    numbers.append(num)

sum_of_numbers = sum(numbers)
print("The sum of the positive numbers is:", sum_of_numbers)
