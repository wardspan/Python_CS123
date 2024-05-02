import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Blackjack")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
deck = []
player_hand = []
dealer_hand = []

# Function to create a new deck of cards
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Function to deal a card to a hand
def deal_card(hand):
    card = deck.pop()
    hand.append(card)

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ["J", "Q", "K"]:
            value += 10
        elif rank == "A":
            value += 11
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

# Function to draw the game screen
def draw_screen():
    window.fill(BLACK)
    # Draw player's hand
    for i, card in enumerate(player_hand):
        card_text = font.render(card[0] + " of " + card[1], True, WHITE)
        window.blit(card_text, (20, 20 + i * 40))
    # Draw dealer's hand
    for i, card in enumerate(dealer_hand):
        card_text = font.render(card[0] + " of " + card[1], True, WHITE)
        window.blit(card_text, (20, 300 + i * 40))
    pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a new deck if the current deck is empty
    if len(deck) == 0:
        deck = create_deck()

    # Deal initial cards
    if len(player_hand) == 0 and len(dealer_hand) == 0:
        deal_card(player_hand)
        deal_card(dealer_hand)
        deal_card(player_hand)
        deal_card(dealer_hand)

    # Calculate hand values
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Draw the game screen
    draw_screen()

# Quit the game
pygame.quit()