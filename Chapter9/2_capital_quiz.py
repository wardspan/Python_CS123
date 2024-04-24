
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values. The program should then randomly quiz the user by displaying
# the name of a state and asking the user to enter that state’s capital. The program should
# keep a count of the number of correct and incorrect responses.

import random
    
def main():
    states_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }
    
    correct_count = 0
    incorrect_count = 0

    while True:
        state = random.choice(list(states_capitals.keys()))
        capital = input(f"What is the capital of {state}? ")
        
        if capital == states_capitals[state]:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect. The capital of {state} is {states_capitals[state]}.")
            incorrect_count += 1
            
        choice = input("Continue? (y/n) ")
        if choice.lower() != "y":
            break
        
        print(f"Correct responses: {correct_count}")
        print(f"Incorrect responses: {incorrect_count}")

    
if __name__ == "__main__":
    main()
    