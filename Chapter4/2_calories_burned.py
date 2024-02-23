# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that 
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

print("This program will compute how many calories you burn running on a treadmill")
print("The program will assume that you are burning 4.2 calories per minute")

minutes = 10

for minutes in range(10, 31, 5):
    calories_burned = minutes * 4.2
    print(f"Calories burned after {minutes} minutes is {calories_burned}")

# Display the total number of calories burned
total_calories_burned = 30 * 4.2
print(f"The total number of calories burned is {total_calories_burned}")
# End of program