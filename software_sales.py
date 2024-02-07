print("Buy more and save more with our software sales program!")
print("This program will calculate the discount on your purchase based on the number of units you buy.")
units = int(input("Enter the number of units you would like to purchase: "))
if units >=10 and units < 19:
    discount = .10
elif units >=20 and units < 49:
    discount = .20
elif units >=50 and units < 99:
    discount = .30
else:
    discount = .40
total_cost = units * 99
total_cost_discount = units * 99 * (1 - discount)
savings = total_cost - total_cost_discount
print(f"You have earned a {discount * 100:.0f}% discount on your purchase.") # display the discount
print(f"The total cost of your purchase before discount is ${total_cost:.2f}")  # display the total cost
print(f"The total cost of your purchase after discount is ${total_cost_discount:.2f}")  # display the discount cost
print(f"You saved ${savings:.2f} today!")  # display the savings cost
print("Goodbye!")