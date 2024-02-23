# Write a program that calculates the amount of money a person would earn over a period 
# of time if his or her salary is one penny the first day, two pennies the second day, 
# and continues to double each day. The program should ask the user for the number of days. 
# Display a table showing what the salary was for each day, then show the total pay at the 
# end of the period. The output should be displayed in a dollar amount, not the number of pennies.

num_days = int(input("Enter the number of days: "))

salary = 0
total_pay = 0

print("Day\tSalary")
print("-----------------")

for day in range(1, num_days + 1):
    salary = 2 ** (day - 1)
    total_pay += salary
    print(f"{day}\t${salary / 100:.2f}")

print("-----------------")
print(f"Total pay: ${total_pay / 100:.2f}")