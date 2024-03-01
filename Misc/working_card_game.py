"""
Write a python program utilizing functions that randomly deals two players two
cards a piece. The players are awarded points for the cards where the rank
equals the points unless it is a face card.
    - ace equals 20 points.
    - king equals 13 points.
    - queen equals 12 points.
    - jack equals 11 points.
    - 100 bonus points if the two cards are of the same rank.
    - 70 bonus points if the cards are in sequence and same suit.
    - 50 bonus points if the cards are in sequence but a different suit.
Calculate total points plus bonus points for each player, and print the
cards rank and suit number for each player. Compare the total points of two
players and announce the winner, the player with higher points.
"""

import random


def deal_cards():
    """
    Deal two cards to a player.
    """
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    cards = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(cards)
    return cards[:2]


def calculate_points(cards):
    """
    Calculate the points based on the ranks of the cards.
    """
    points = 0
    ranks = [card[0] for card in cards]

    for rank in ranks:
        if rank.isdigit():
            points += int(rank)
        elif rank == "A":
            points += 20
        elif rank == "K":
            points += 13
        elif rank == "Q":
            points += 12
        elif rank == "J":
            points += 11

    return points


def calculate_bonus_points(cards):
    """
    Calculate the bonus points based on the ranks and suits of the cards.
    """
    bonus_points = 0
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    if ranks[0] == ranks[1]:
        bonus_points += 100
    elif (ranks[0], ranks[1]) in [("2", "3"), ("3", "4"), ("4", "5"), ("5", "6"), ("6", "7"), ("7", "8"), ("8", "9"), ("9", "10"), ("10", "J"), ("J", "Q"), ("Q", "K"), ("K", "A")] and suits[0] != suits[1]:
        bonus_points += 50
    elif (ranks[0], ranks[1]) in [("A", "K"), ("K", "Q"), ("Q", "J"), ("J", "10"), ("10", "9"), ("9", "8"), ("8", "7"), ("7", "6"), ("6", "5"), ("5", "4"), ("4", "3"), ("3", "2") ] and suits[0] != suits[1]:
        bonus_points += 50
    elif (ranks[0], ranks[1]) in [("2", "3"), ("3", "4"), ("4", "5"), ("5", "6"), ("6", "7"), ("7", "8"), ("8", "9"), ("9", "10"), ("10", "J"), ("J", "Q"), ("Q", "K"), ("K", "A")] and suits[0] == suits[1]:
        bonus_points += 70
    elif (ranks[0], ranks[1]) in [("A", "K"), ("K", "Q"), ("Q", "J"), ("J", "10"), ("10", "9"), ("9", "8"), ("8", "7"), ("7", "6"), ("6", "5"), ("5", "4"), ("4", "3"), ("3", "2") ] and suits[0] == suits[1]:
        bonus_points += 70
    return bonus_points


def print_cards(player, cards):
    """
    Print the cards of a player.
    """
    print(f"Player {player} cards:")
    for card in cards:
        print(f"Rank: {card[0]}, Suit: {card[1]}")

def main():
    # Deal cards to players
    player1_cards = deal_cards()
    player2_cards = deal_cards()

    # Calculate points for each player
    player1_points = calculate_points(player1_cards)
    player1_bonus = calculate_bonus_points(player1_cards)
    player1_total = player1_points + player1_bonus
    player2_points = calculate_points(player2_cards)
    player2_bonus = calculate_bonus_points(player2_cards)
    player2_total = player2_points + player2_bonus

    # Print the cards for each player
    print_cards(1, player1_cards)
    print("Points:", player1_points)
    print("Bonus points:", player1_bonus)
    print("Total points:", player1_points + player1_bonus)
    print()
    print_cards(2, player2_cards)
    print("Points:", player2_points)
    print("Bonus points:", player2_bonus)
    print("Total points:", player2_points + player2_bonus)
    print()

    # Compare total points and announce the winner
    if player1_total > player2_total:
        print("Player 1 wins!")
    elif player2_total > player1_total:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
