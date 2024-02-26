# This program converts cups to fluid ounces.

def main():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups: '))
    # Convert the cups to ounces. cups_to_ounces(cups_needed)
    cups_to_ounces(cups_needed)
    
def intro():
    print('This program converts measurements in cups to fluid ounces.')
    print('For your reference the formula is:')
    print('1 cup = 8 fluid ounces')
    print()
    
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces.')
    
# Call the main function.
main()
