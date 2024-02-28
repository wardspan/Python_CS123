# Write a program that calls a procedure to calculate the electricity bill. 
# The program does the following steps prompts the user for the amount of 
# electricity used in kilowatt-hour. prompts the user for the cost of electricity 
# per kilowatt-hour. It calculates the total amount of the electric bill which 
# includes an 8% sales tax. Print the total amount of electricity bill.

#Procedure definition of calculate_ebill( )
def calculate_ebill(cost_per_kwh, amount, tax):
    total_cost = usage * cost_per_kwh
    sales_tax = total_cost * 0.08
    total_bill = total_cost + sales_tax
    return total_bill

usage = float(input("Enter the amount of electricity used in kilowatt-hour: "))
cost_per_kwh = float(input("Enter the cost of electricity per kilowatt-hour: "))

bill = calculate_ebill(usage, cost_per_kwh)
print("Total electricity bill: $", bill)