# Write a program which simulates the game of cards. The game that you create has two players and each one picks two cards.
# The players are awarded points for the cards using the rules given below. Calculate total points for each player and at
# the end print the cards rank and suit number for each player. Compare the total points of two players and announce the winner,
# the player with higher points. The points for a card equal the rank of the card unless it’s an Ace. For face cards the
# points are ace 20, king 13, queen 12 and the jack has 11 points. The additional points are awarded as:
# 1.	Two cards of same rank 100 points.
# 2.	Two cards in a sequence and same suit 70 points.
# 3.	Two cards in a sequence but different suit 50 points.

import random

# Define the ranks and suits of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['♠', '♥', '♦', '♣']
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

# Function to calculate the points for a card
def calculate_points(rank: str) -> int:
    return values[rank]

# Function to check if two cards are in sequence
def is_sequence(card1: str, card2: str) -> bool:
    return abs(ranks.index(card1) - ranks.index(card2)) == 1

# Function to check if two cards have the same suit
def is_same_suit(card1, card2):
    return card1.split(' ')[-1] == card2.split(' ')[-1]

# Function to calculate additional points based on the rules
def calculate_additional_points(card1, card2):
    additional_points = 0
    if card1.split(' ')[0] == card2.split(' ')[0]:
        additional_points += 100
    return additional_points

# Function to simulate the card game
def simulate_card_game():
    # Initialize the players' cards and points
    player1_cards = []
    player2_cards = []
    player1_points = 0
    player2_points = 0

    # Each player picks two cards
    for _ in range(2):
        card1 = random.choice(ranks) + ' ' + random.choice(suits)
        card2 = random.choice(ranks) + ' ' + random.choice(suits)
        player1_cards.append(card1)
        player2_cards.append(card2)
        player1_points += calculate_points(card1.split(' ')[0])
        player2_points += calculate_points(card2.split(' ')[0])
        player1_points += calculate_additional_points(card1, card2)
        player2_points += calculate_additional_points(card1, card2)

    # Print the cards and points for each player
    print("Player 1 cards:", player1_cards)
    print("Player 1 points:", player1_points)
    print("Player 2 cards:", player2_cards)
    print("Player 2 points:", player2_points)

    # Compare the total points and announce the winner
    if player1_points > player2_points:
        print("Player 1 wins!")
    elif player2_points > player1_points:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Run the card game simulation
simulate_card_game()