"""
Write a program which simulates the game of cards.
The game that you create has two players and each one picks two cards.
The players are awarded points for the cards using the rules given below.
Calculate total points for each player and at the end print the cards rank and suit number for each player.
Compare the total points of two players and announce the winner, the player with higher points.
The points for a card equal the rank of the card unless it’s an Ace.
For face cards the points are ace 20, king 13, queen 12 and the jack has 11 points.
The additional points are awarded as:
1. Two cards of same rank 100 points.
2. Two cards in a sequence and same suit 70 points.
3. Two cards in a sequence but different suit 50 points.
"""

import random

# Define the ranks and suits of the cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal two cards to each player
player1_cards = [deck.pop() for _ in range(2)]
player2_cards = [deck.pop() for _ in range(2)]

# Calculate points for each player
player1_points = 0
player2_points = 0

for card in player1_cards:
    rank, suit = card
    if rank == 'Ace':
        player1_points += 20
    elif rank in ['King', 'Queen', 'Jack']:
        player1_points += {'King': 13, 'Queen': 12, 'Jack': 11}[rank]
    else:
        player1_points += int(rank)

for card in player2_cards:
    rank, suit = card
    if rank == 'Ace':
        player2_points += 20
    elif rank in ['King', 'Queen', 'Jack']:
        player2_points += {'King': 13, 'Queen': 12, 'Jack': 11}[rank]
    else:
        player2_points += int(rank)

# Check for additional points
if player1_cards[0][0] == player1_cards[1][0]:
    player1_points += 100

if player2_cards[0][0] == player2_cards[1][0]:
    player2_points += 100

if abs(ranks.index(player1_cards[0][0]) - ranks.index(player1_cards[1][0])) == 1 and player1_cards[0][1] == player1_cards[1][1]:
    player1_points += 70
elif abs(ranks.index(player1_cards[0][0]) - ranks.index(player1_cards[1][0])) == 1:
    player1_points += 50

if abs(ranks.index(player2_cards[0][0]) - ranks.index(player2_cards[1][0])) == 1 and player2_cards[0][1] == player2_cards[1][1]:
    player2_points += 70
elif abs(ranks.index(player2_cards[0][0]) - ranks.index(player2_cards[1][0])) == 1:
    player2_points += 50

# Print the cards and points for each player
print(f"Player 1 cards: {player1_cards}")
print(f"Player 1 points: {player1_points}")

print(f"Player 2 cards: {player2_cards}")
print(f"Player 2 points: {player2_points}")

# Determine the winner
if player1_points > player2_points:
    print("Player 1 wins!")
elif player2_points > player1_points:
    print("Player 2 wins!")
else:
    print("It's a tie!")