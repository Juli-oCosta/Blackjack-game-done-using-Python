# ----------------------------------------------------------------------------------------------------------------
# Needed changes according to the game rules:

# In a blackjack game, the dealer must keep drawing cards until his hand value is at least 17.
# The dealer may only draw new cards once the player hits 'stand'.
# The dealer's hand remains partially hidden (showing only one card) while the player is still making choices.
# Once the player chooses "Stand", the dealer reveals their full hand and continues drawing cards until reaching at least 17.
# This keeps the tension and uncertainty regarding the dealer's final hand.

# Remove Dealer's Hand Display During Play:
# Only show the first hidden card (hidden as '?') and second card.

# Reveal dealer's full hand only after the player's option is "Stand"
# The dealer's hand value can then be calculated and displayed.
# ----------------------------------------------------------------------------------------------------------------
# About the Ace:

# If an Ace is able to be worth 11, without busting the total (21), then it's worthy 11.
# Otherwise, it's worthy 1.
# ----------------------------------------------------------------------------------------------------------------

import random

# 🍀 Defining the game cards and their values
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
card_values = {}
game_start = True

# Assigning point values to each card
for card in cards:
    if card == 'A':
        card_values[card] = 1  # Ace is initially counted as 1
    elif card in ['J', 'K', 'Q']:
        card_values[card] = 10  # Face cards (Jack, King, Queen) are worth 10
    else:
        card_values[card] = int(card)  # Number cards have their face value

# Restarts the game when it ends, based on player's choice
def restart_game():
    restart_choice = int(input("\nDo you want to play again? \n1 - Yes. \n2 - No.\nChoice: "))
    if restart_choice == 1:
        # Reset hands and start a new game
        player_hand = random.sample(cards, 2)
        dealer_hand = random.sample(cards, 2)
        dealer_initial_display = ["?"] + dealer_hand[1:]
        
        print("\n🍀 Starting a new game 🍀")
        print(f"Your starting hand: {', '.join(player_hand)}")
        print(f"Dealer shows: {', '.join(dealer_initial_display)}")

        game_choice(player_hand, dealer_hand)  # Restart the game loop
    else:
        print("\nThanks for playing!")

# 🍀 Starting the game and deciding each player's initial hands
print("🍀 Welcome to our Blackjack game 🍀\n")

# 🍀 Function to calculate the value of a given hand
def calculate_hand_value(hand):
    total = 0
    ace_count = 0

    # Summing the values of the cards
    for card in hand:
        total += card_values[card]
        if card == 'A':
            ace_count += 1

    # Adjusting the value of aces if it benefits the player (1 or 11)
    while ace_count > 0 and total + 10 <= 21:
        total += 10
        ace_count -= 1

    return total


# 🍀 Function to manage player decisions (Hit or Stand)
def game_choice(player_hand, dealer_hand):
    global game_start
    while True:
        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        try:
            # Prompting the player for their next move
            player_game_choice = int(input("\nWhat do you want to do? \n1 - Hit\n2 - Stand\nChoice: "))
        except ValueError:
            print("Enter a valid option.")
            continue

        # 🍀 Hit (Draw a new card)
        if player_game_choice == 1:
            new_card = random.choice(cards)
            player_hand.append(new_card)
            print(f"\nYou drew a {new_card}")
            print(f"Your hand now: {', '.join(player_hand)}")
            player_score = calculate_hand_value(player_hand)

            # Dealer draws a new card if their score is less than 17
            if dealer_score < 17:
                new_card_dealer = random.choice(cards)
                dealer_hand.append(new_card_dealer)
                print("Dealer drew a new card.")

            # Displaying the dealer's hand with one card hidden
            dealer_hand_display = ["?"] + dealer_hand[1:]
            print(f"Dealer's hand: {', '.join(dealer_hand_display)}")

            # Check if the player has exceeded 21 (busted)
            if player_score > 21:
                print("\n🔴 You lost 🔴")
                print(f"Your final hand: {', '.join(player_hand)}")
                print(f"Dealer's final hand: {', '.join(dealer_hand)}")

                restart_game()

                break

        # 🍀 Stand (End player's turn and reveal dealer's hand)
        elif player_game_choice == 2:
            print("\nYou chose to stand.")

            # Revealing both hands
            print(f"Your final hand: {', '.join(player_hand)}")
            print(f"Your score: {player_score}")
            print(f"\nDealer's final hand: {', '.join(dealer_hand)}")
            print(f"Dealer's score: {dealer_score}")

            # Determining the game outcome
            if player_score > 21:
                print("🔴 You lost 🔴")
            elif player_score == 21 or player_score > dealer_score:
                print("🍀 You won 🍀")
            elif player_score < dealer_score and dealer_score > 21:
                print("🍀 You won 🍀")
            elif player_score == dealer_score and player_score <= 21:
                print("🃏 It's a draw 🃏")
            else:
                print("🔴 Dealer won 🔴")

            restart_game()
            
            break

        else:
            print("Invalid choice! Please choose 1 or 2.")

# Initialize player and dealer hands
player_hand = random.sample(cards, 2)
dealer_hand = random.sample(cards, 2)

# Display the initial hands (dealer shows only one card)
dealer_initial_display = ["?"] + dealer_hand[1:]

print(f"Your starting hand: {', '.join(player_hand)}")
print(f"Dealer shows: {', '.join(dealer_initial_display)}")

# Start the game loop
if game_start:
    game_choice(player_hand, dealer_hand)

