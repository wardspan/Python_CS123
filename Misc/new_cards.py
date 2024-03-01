# Write a program which simulates the game of cards. The game that you create has two players and each one picks two cards.  
# The players are awarded points for the cards using the rules given below. Calculate total points for each player and at 
# the end print the cards rank and suit number for each player. Compare the total points of two players and announce the winner, 
# the player with higher points. The points for a card equal the rank of the card unless it’s an Ace. For face cards the 
# points are ace 20, king 13, queen 12 and the jack has 11 points. The additional points are awarded as: 
# 1.	Two cards of same rank 100 points.
# 2.	Two cards in a sequence and same suit 70 points.
# 3.	Two cards in a sequence but different suit 50 points.

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
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


def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    random.shuffle(deck)
    return deck


def deal_cards(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        hand.append(deck.pop())
    return hand


def calculate_card_value(card):
    rank, _ = card
    if rank in values:
        return values[rank]
    else:
        return 20


def calculate_bonus_points(hand):
    rank_set = set([rank for _, rank in hand])
    suit_set = set([suit for suit, _ in hand])

    # Check for same rank bonus
    if len(rank_set) == 1:
        return 100

    # Check for sequence bonus
    ranks_sorted = sorted([calculate_card_value(card) for card in hand])
    if ranks_sorted[1] == ranks_sorted[0] + 1:
        if len(suit_set) == 1:
            return 70
        else:
            return 50

    return 0


def play_game():
    deck = create_deck()

    # Deal cards to players
    player1_hand = deal_cards(deck, 2)
    player2_hand = deal_cards(deck, 2)

    # Calculate card values and bonus points
    player1_values = [calculate_card_value(card) for card in player1_hand]
    player2_values = [calculate_card_value(card) for card in player2_hand]
    player1_points = sum(player1_values) + calculate_bonus_points(player1_hand)
    player2_points = sum(player2_values) + calculate_bonus_points(player2_hand)

    # Print player cards and points
    print("Player 1:")
    for card in player1_hand:
        suit, rank = card
        print(f"- {rank} of {suit}")
    print(f"Total points: {player1_points}\n")

    print("Player 2:")
    for card in player2_hand:
        suit, rank = card
        print(f"- {rank} of {suit}")
    print(f"Total points: {player2_points}\n")

    # Declare winner
    if player1_points > player2_points:
        print("Player 1 wins!")
    elif player1_points < player2_points:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()
