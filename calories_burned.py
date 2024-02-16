print("This program will compute how many calories you burn running on a treadmill")
print("The program will assume that you are burning 4.2 calories per minute")

minutes = 10
# Get the number of calories burned each 5 minutes
for minutes in range(10, 31, 5):
    calories_burned = minutes * 4.2
    minutes = minutes + 5
    print(f"Calories burned after {minutes} minutes is {calories_burned}")
# Display the total number of calories burned
print(f"The total number of calories burned is {calories_burned}")
# End of program