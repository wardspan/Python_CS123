# This program gets a password from the user and validates it.
import login


def main():
    """
    This function gets a password from the user and validates it.
    """
    # Get a password from the user.
    password = input('Enter your password: ')
    
    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')
    
    # Print a message indicating that the password is valid.
    print('That is a valid password.')


# Call the main function.
if __name__ == '__main__':
    main()

