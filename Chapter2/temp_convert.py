print("Welcome to the temperature converter!")
temp_choice = input("Would you like to convert from Celsius to Fahrenheit (C to F) or Fahrenheit to Celsius (F to C)? ")
if temp_choice == "C to F":
    print("Let's convert some temperatures from Celsius to Fahrenheit!")
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius * 9.0/5.0) + 32
    print("Temperature:", celsius, "Celsius = ", fahrenheit, " F")
elif temp_choice == "F to C":
    print("Let's convert some temperatures from Fahrenheit to Celsius!")
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print("Temperature:", fahrenheit, "Fahrenheit = ", celsius, " C")
else:
    print("Invalid input. Please try again.")
print("Goodbye!")