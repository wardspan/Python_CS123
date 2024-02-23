# Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled.
# It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. 

# Get the speed of the vehicle from the user
speed = float(input("Enter the speed of the vehicle (in miles per hour): "))

# Get the number of hours traveled from the user
hours = int(input("Enter the number of hours the vehicle has traveled: "))

# Display the distance traveled for each hour
print("Hour\tDistance Traveled")
print("------------------------")
for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"{hour}\t{distance} miles")