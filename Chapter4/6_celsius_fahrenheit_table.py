# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents.

print("Celsius\tFahrenheit")
print("-------------------")
for celsius in range(21):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t{fahrenheit}")