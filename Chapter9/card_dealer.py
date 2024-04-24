# This program uses a dictionary as a deck of cards.

import random

def main():
    deck = create_deck()
    num_cards = int(input("How many cards should I deal? "))
    deal_cards(deck, num_cards)
    
def create_deck():
    deck = {'Ace of ♠': 1, '2 of ♠': 2, '3 of ♠': 3, '4 of ♠': 4, '5 of ♠': 5,
            '6 of ♠':6, '7 of ♠': 7, '8 of ♠': 8, '9 of ♠': 9, '10 of ♠': 10,
            'Jack of ♠': 10, 'Queen of ♠': 10, 'King of ♠': 10,
            
            'Ace of ♥': 1, '2 of ♥': 2, '3 of ♥': 3, '4 of ♥': 4, '5 of ♥': 5,
            '6 of ♥':6, '7 of ♥': 7, '8 of ♥': 8, '9 of ♥': 9, '10 of ♥': 10,
            'Jack of ♥': 10, 'Queen of ♥': 10, 'King of ♥': 10,
            
            'Ace of ♣': 1, '2 of ♣': 2, '3 of ♣': 3, '4 of ♣': 4, '5 of ♣': 5,
            '6 of ♣':6, '7 of ♣': 7, '8 of ♣': 8, '9 of ♣': 9, '10 of ♣': 10,
            'Jack of ♣': 10, 'Queen of ♣': 10, 'King of ♣': 10,
            
            'Ace of ♦': 1, '2 of ♦': 2, '3 of ♦': 3, '4 of ♦': 4, '5 of ♦': 5,
            '6 of ♦':6, '7 of ♦': 7, '8 of ♦': 8, '9 of ♦': 9, '10 of ♦': 10,
            'Jack of ♦': 10, 'Queen of ♦': 10, 'King of ♦': 10}
    return deck

def deal_cards(deck, num_cards):
    hand_value = 0
    
    if num_cards > len(deck):
        num_cards = len(deck)
        
    for count in range(num_cards):
        card = random.choice(list(deck.keys()))
        print(card)
        hand_value += deck.pop(card)
        
    print("Value of hand:", hand_value)
    
if __name__ == "__main__":
    main()
    