# Definition of the main function.
def main():
    name = get_name()  # Assign the returned value of get_name() to the variable "name".
    print(f'Hello {name}.')  # Print the value of "name".

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')  # Assign the user input to the variable "name".
    return name  # Return the value of "name".

# Call the main function. 
main()