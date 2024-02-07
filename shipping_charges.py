print("Welcome to Fast Freight Shipping Company")
print("This program will calculate the shipping charges for a package based on its weight.")
weight = float(input("Enter the weight of the package: "))
if weight <= 2:
    shipping_charges = 1.50
elif weight > 2 and weight < 6:
    shipping_charges = 3.00
elif weight >= 6 and weight < 10:
    shipping_charges = 4.00
else:
    shipping_charges = 4.75
print(f"The shipping charges for the package are ${shipping_charges:.2f}") 
print("Goodbye!")