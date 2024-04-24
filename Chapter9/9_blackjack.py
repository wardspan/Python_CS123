# Use card_dealer.py program to simulate a simplified version of the game of Blackjack between 
# two virtual players. The cards have the following values:
# Numeric cards are assigned the value they have printed on them. For example, 
# the value of 2♠ is 2, and the value of the 5♦ is 5.
# Jacks, queens, and kings are valued at 10.
# Aces are valued at 1 or 11, depending on the player’s choice. 
# The program should deal cards to each player until one player’s hand is worth more than 21 points. 
# When that happens, the other player is the winner. (It is possible that both players’ hands 
# will simultaneously exceed 21 points, in which case neither player wins.) The program 
# should repeat until all the cards have been dealt from the deck.
# If a player is dealt an ace, the program should decide the value of the card according to the following rule: 
# The ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. 
# In that case, the ace will be worth 1 point.

import random

# Define the deck of cards
def create_deck():
    deck = {'A♠': 1, '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5,
            '6♠':6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10,
            'J♠': 10, 'Q♠': 10, 'K♠': 10,
            
            'Ace♥': 1, '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5,
            '6♥':6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10,
            'J♥': 10, 'Q♥': 10, 'K♥': 10,
            
            'Ace♣': 1, '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5,
            '6♣':6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10,
            'J♣': 10, 'Q♣': 10, 'K♣': 10,
            
            'Ace♦': 1, '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5,
            '6♦':6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10,
            'J♦': 10, 'Q♦': 10, 'K♦': 10}
    
    return deck

def deal__player_cards(deck):
    player1_value = 0
    player2_value = 0
    
    while deck:
    # Deal a card to player 1
    card = deck.pop()
    player1_hand.append(card)

    # Deal a card to player 2
    card = deck.pop()
    player2_hand.append(card)

    # Calculate the total value of player 1's hand
    player1_total = sum(card_values[card] for card in player1_hand)

    # Calculate the total value of player 2's hand
    player2_total = sum(card_values[card] for card in player2_hand)

    # Check if any player's hand exceeds 21 points
    if player1_total > 21 and player2_total > 21:
        print("Both players' hands exceed 21 points. It's a draw!")
        break
    elif player1_total > 21:
        print("Player 2 wins!")
        break
    elif player2_total > 21:
        print("Player 1 wins!")
        break

def main():
    deck = create_deck()


