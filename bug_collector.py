print("Welcome to the handy dandy bug collector tracker")
print("This program will help you keep track of the bugs you collect every day for a week")
print("Please enter the number of bugs you collect each day for a week")
# Initialize the variables
bugs_collected = 0
days = 7
# Get the number of bugs collected each day
for day in range(1, days + 1):
    bugs_collected += int(input(f"Enter the number of bugs collected on day {day}: "))
# Display the total number of bugs collected
print(f"The total number of bugs collected is {bugs_collected}")
# End of program
