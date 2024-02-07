print("Welcome to the age classifier!")
print("This program will classify a person's age into one of the following categories: infant, child, teenager, adult, or senior.") 
age = int(input("Enter the person's age: "))
if age < 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is a senior.")
print("Goodbye!")