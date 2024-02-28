# Write a program that takes an input from the user and converts temperature 
# from Farenheit scale to celsius scale. It should have a procedure named 
# Fahrenheittocelsius( ) that accepts one parameter Farenheitwhich is temperaturein Farenheit 
# and returns the temperature in Celsius.

def Fahrenheittocelsius(Farenheit):
    celsius = (Farenheit - 32) * 5/9
    return celsius

Farenheit = float(input("Enter temperature in Farenheit: "))
celsius = Fahrenheittocelsius(Farenheit)
print("Temperature in Celsius:", celsius)