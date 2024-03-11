import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ")
    while choice.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock/paper/scissors): ")
    return choice.lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print("Computer's choice:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

play_game()