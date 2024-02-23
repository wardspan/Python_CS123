# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her 
# expenses for the month and keep a running total. When the loop finishes, the program should 
# display the amount that the user is over or under budget.

print("This program will help you analyze your budget for the month.")
budget = float(input("Enter your budget for the month: "))
total_expenses = 0

while True:
    expense = float(input("Enter an expense (or 0 to finish): "))
    if expense == 0:
        break
    total_expenses += expense

difference = budget - total_expenses

if difference > 0:
    print("You are under budget by $", difference)
elif difference < 0:
    print("You are over budget by $", abs(difference))
else:
    print("You are exactly on budget!")