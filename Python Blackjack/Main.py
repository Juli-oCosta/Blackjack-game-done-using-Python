# Alterações:

# No Blackjack, o dealer deve comprar cartas até que sua mão alcance pelo menos 17.
# Portanto, uma abordagem comum é ocultar a mão do dealer até que o jogador decida "stand".
# Assim, você mantém a tensão e a incerteza sobre a mão do dealer.

# Sugestões

# Remova a Exibição da Mão do Dealer Durante a Jogada:
# Apenas mostre a primeira carta oculta (indicada como "?") e a segunda carta.

# Revele a Mão do Dealer Após o Jogador Optar por "Stand": Quando o jogador escolher "stand",
# você pode calcular a mão do dealer e exibi-la.

# Considerações:

# Se um Ás puder ser 11 sem estourar o total (21), ele vale 11; caso contrário, ele vale 1.

import random

# 🍀Defining the game cards and it's values
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
card_values = {}
game_start = True

for card in cards:
    if card == 'A':
        card_values[card] = 1
    elif card in ['J', 'K', 'Q']:
        card_values[card] = 10
    else:
        card_values[card] = int(card)

# 🍀Starting the game and deciding each other their respective initial hands
print("🍀Welcome to our Blackjack game🍀\n")

player_cards_choice = random.sample(cards, 2)
dealer_cards_choice = random.sample(cards, 2)


# 🍀Calculating the hands
def calculate_hand_value(hand):
    total = 0
    ace_count = 0

    for card in hand:
        total += card_values[card]
        if card == 'A':
            ace_count += 1

    # Special treatment for the ace, which can be worth 1 or 11 depending on the current hand
    while ace_count > 0 and total + 10 <= 21:
        total += 10
        ace_count -= 1

    return total


# 🍀Hit or stand
def game_choice(player_hand, dealer_hand):
    global game_start
    while True:
        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        try:
            player_game_choice = int(input("\nWhat do you want to do? \n1 - Hit.\n2 - Stand\nChoice: "))
        except ValueError:
            print("Enter a valid option.")
            continue

        # 🍀Hit
        if player_game_choice == 1:
            new_card = random.choice(cards)
            player_hand.append(new_card)
            print(f"\nYou drew a {new_card}")
            print(f"Your hand now: {', '.join(player_hand)}")
            player_score = calculate_hand_value(player_hand)

            if dealer_score < 17:
                new_card_dealer = random.choice(cards)
                dealer_hand.append(new_card_dealer)
                print(f"Dealer drew a new card.")

            dealer_hand_display = ["?"] + dealer_hand[1:]
            print(f"Dealer's hand: {', '.join(dealer_hand_display)}")

            if player_score > 21:
                print("\n🔴You lost🔴")
                print(f"Your final hand: {', '.join(player_hand)}")
                print(f"Dealer's final hand: {', '.join(dealer_hand)}")
                break

        # 🍀Stand
        elif player_game_choice == 2:
            print("\nYou chose to stand.")

            print(f"Your final hand: {', '.join(player_hand)}")
            print(f"Your score: {player_score}")
            print(f"\nDealer's final hand: {', '.join(dealer_hand)}")
            print(f"Dealer's score: {dealer_score}")

            if player_score > 21:
                print("🔴You lost🔴")
                game_start = False
            elif player_score == 21 or player_score > dealer_score:
                print("🍀You won🍀")
                game_start = False
            elif player_score < dealer_score and dealer_score > 21:
                print("🍀You won🍀")
                game_start = False
            elif player_score == dealer_score and player_score <= 21:
                print("🃏It's a draw🃏")
                game_start = False
            else:
                print("🔴Dealer won🔴")
                game_start = False

                break
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


player_hand = random.sample(cards, 2)
dealer_hand = random.sample(cards, 2)

dealer_initial_display = ["?"] + dealer_hand[1:]

print(f"Your starting hand: {', '.join(player_hand)}")
print(f"Dealer shows: {', '.join(dealer_initial_display)}")

if game_start:
    game_choice(player_hand, dealer_hand)