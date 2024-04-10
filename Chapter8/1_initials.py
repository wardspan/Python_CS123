# Write a program that gets a string containing a person’s first, middle, and last names, 
# and displays their first, middle, and last initials. For example, if the user enters 
# John William Smith, the program should display J. W. S.

def main():
    """
    This program gets a string containing a person's first, middle, and last names,
    and displays their first, middle, and last initials.
    """
    # Get the full name from the user
    full_name = input("Enter your full name: ")

    # Split the full name into a list of names
    names = full_name.split()

    # Initialize an empty string to store the initials
    initials = ""

    # Iterate over each name in the list
    for name in names:
        # Get the first character of each name and convert it to uppercase
        initial = name[0].upper()
        # Add the initial to the initials string
        initials += initial + ". "

    # Remove the trailing space from the initials string
    initials = initials.strip()

    # Display the initials
    print("Initials:", initials)

if __name__ == "__main__":
    main()