"""
Use card_dealer.py program to simulate a simplified version of the game of Blackjack between two virtual players.
The cards have the following values:
- Numeric cards are assigned the value they have printed on them.
- Jacks, queens, and kings are valued at 10.
- Aces are valued at 1 or 11, depending on the player’s choice.
The program should deal cards to each player until one player’s hand is worth more than 21 points.
When that happens, the other player is the winner.
(It is possible that both players’ hands will simultaneously exceed 21 points, in which case neither player wins.)
The program should repeat until all the cards have been dealt from the deck.
If a player is dealt an ace, the program should decide the value of the card according to the following rule:
The ace will be worth 11 points, unless that makes the player’s hand exceed 21 points. In that case, the ace will be worth 1 point.
"""

import random

def create_deck():
    """
    Create a deck of cards using a list.
    """
    deck = ['Ace of ♠', '2 of ♠', '3 of ♠', '4 of ♠', '5 of ♠', '6 of ♠', '7 of ♠', '8 of ♠', '9 of ♠', '10 of ♠', 'Jack of ♠', 'Queen of ♠', 'King of ♠',
        'Ace of ♥', '2 of ♥', '3 of ♥', '4 of ♥', '5 of ♥', '6 of ♥', '7 of ♥', '8 of ♥', '9 of ♥', '10 of ♥', 'Jack of ♥', 'Queen of ♥', 'King of ♥',
        'Ace of ♣', '2 of ♣', '3 of ♣', '4 of ♣', '5 of ♣', '6 of ♣', '7 of ♣', '8 of ♣', '9 of ♣', '10 of ♣', 'Jack of ♣', 'Queen of ♣', 'King of ♣',
        'Ace of ♦', '2 of ♦', '3 of ♦', '4 of ♦', '5 of ♦', '6 of ♦', '7 of ♦', '8 of ♦', '9 of ♦', '10 of ♦', 'Jack of ♦', 'Queen of ♦', 'King of ♦']
    return deck

def deal_card(deck):
    """
    Deal a random card from the deck.
    """
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(hand):
    """
    Calculate the score of a player's hand.
    """
    score = 0
    num_aces = 0
    
    for card in hand:
        if card.startswith('Ace'):
            num_aces += 1
        elif card.startswith('2') or card.startswith('3') or card.startswith('4') or card.startswith('5') or card.startswith('6') or card.startswith('7') or card.startswith('8') or card.startswith('9'):
            score += int(card.split()[0])
        else:
            score += 10
    
    for _ in range(num_aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    
    return score

def main():
    deck = create_deck()
    player1_hand = []
    player2_hand = []
    
    while len(deck) > 0:
        player1_hand.append(deal_card(deck))
        player2_hand.append(deal_card(deck))
        
        player1_score = calculate_score(player1_hand)
        player2_score = calculate_score(player2_hand)
        
        if player1_score > 21 and player2_score > 21:
            print("Both players have exceeded 21 points. It's a draw!")
            break
        elif player1_score > 21:
            print("Player 2 wins!")
            break
        elif player2_score > 21:
            print("Player 1 wins!")
            break
    
    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", player2_hand)
    print("Player 1's score:", player1_score)
    print("Player 2's score:", player2_score)
    
if __name__ == "__main__":
    main()