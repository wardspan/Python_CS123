import random

def guess_number():
    random_number = random.randint(1, 100)
    num_guesses = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1

        if user_guess > random_number:
            print("Too high! Try again.")
        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} tries.")
            break

guess_number()