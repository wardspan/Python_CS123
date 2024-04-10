# This python program reads the data from the expenses.txt formatted as one expense:cost per line and uses matplotlib 
# to plot a pie chart showing how you spent your money.

import matplotlib.pyplot as plt

def get_expenses():
    expenses = {}
    with open('expenses.txt', 'r') as file:
        for line in file:
            expense, cost = line.strip().split(':')
            expenses[expense] = float(cost)
    return expenses

def main():
    expenses = get_expenses()
    
    # Plot the pie chart
    plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
    plt.title('Expenses')
    plt.show()

if __name__ == '__main__':
    main()
    