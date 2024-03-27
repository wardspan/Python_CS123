# Design a program that asks the user to enter a store’s sales for each day of the week. 
# The amounts should be stored in a list.
# Use a loop to calculate the total sales for the week and display the result.

def main():
    sales = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for day in days:
        sales_amount = float(input(f"Enter sales amount for {day}: "))
        sales.append(sales_amount)
    
    total_sales = sum(sales)
    print(f"Total sales for the week: ${total_sales}")

if __name__ == '__main__':
    main()