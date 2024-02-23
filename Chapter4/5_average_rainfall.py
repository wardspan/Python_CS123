# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will 
# ask the user for the inches of rainfall for that month. After all iterations, the program should display 
# the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

total_rainfall = 0
num_months = 0

num_years = int(input("Please enter the number of years to calculate: "))

for year in range(num_years):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month} of year {year + 1}: "))
        total_rainfall += rainfall
        num_months += 1

average_rainfall = total_rainfall / num_months

print(f"Number of months: {num_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall}")