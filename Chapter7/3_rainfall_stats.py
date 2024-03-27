# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, the average monthly
# rainfall, the months with the highest and lowest amounts.


def main():
    # Create an empty list to store the rainfall data
    rainfall = []

    # Prompt the user to enter the rainfall for each month
    for month in range(1, 13):
        rainfall.append(float(input(f"Enter the rainfall for month {month}: ")))

    # Calculate the total rainfall for the year
    total_rainfall = sum(rainfall)

    # Calculate the average monthly rainfall
    average_rainfall = total_rainfall / len(rainfall)

    # Find the month with the highest rainfall
    max_rainfall = max(rainfall)
    max_month = rainfall.index(max_rainfall) + 1

    # Find the month with the lowest rainfall
    min_rainfall = min(rainfall)
    min_month = rainfall.index(min_rainfall) + 1

    # Display the results
    print(f"Total rainfall for the year: {total_rainfall}")
    print(f"Average monthly rainfall: {average_rainfall}")
    print(f"Month with the highest rainfall: {max_month}")
    print(f"Month with the lowest rainfall: {min_month}")
 
if __name__ == '__main__':
    main()
    