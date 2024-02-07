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
print(f"The discount on your purchase is {discount:.0%}.")
print("Goodbye!")  # display goodbye message    