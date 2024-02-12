"""Write a program to compare two numbers. It should 
a)	Define two numbers.
b)	Compare the two numbers. 
c)	Print the greater of two numbers.
d)	If numbers are equal it should print “Numbers are equal”. """

print("Welcome to the number comparer!")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
if number1 > number2:
    print("The first number", number1, " is greater than the second number.", number2)
elif number1 < number2:
    print("The second number", number2, " is greater than the first number.", number1)
else:
    print("The numbers are equal.")
print("Goodbye!")


