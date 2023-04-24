#Blackjack
import random
from blackjacklogo import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


kart = int(len(cards)) - 1
endgame = False

def hit_for_player():
    global playerscore
    random_player = random.randint(0, kart)
    player_card.append(cards[random_player])
    playerscore = sum(player_card)
    if playerscore > 21:
        if ace in player_card:
            index = player_card.index(ace)
            player_card[index] = new_ace

def hit_for_dealer():
    global dealerscore
    random_dealer = random.randint(0, kart)
    dealer_card.append(cards[random_dealer])
    dealerscore = sum(dealer_card)
    if dealerscore > 21:
        if ace in dealer_card:
            index = dealer_card.index(ace)
            dealer_card[index] = new_ace

def first_hand():
    for i in range(0,2):
        hit_for_player()
        hit_for_dealer()

def yes_or_no(playagain):

    if playagain == "n":
        return True
    else:
        return False

while not endgame: #endgame false olduğu sürece döngü çalışır
    print(logo)
    player_card = []
    dealer_card = []
    ace = 11
    new_ace = 1
    game_start = input("Do you want to play BlackJack? Type 'y' for yes or 'n' for no: ")
    if game_start == "y":
        endgame = False
    else:
        endgame = True

    if endgame == False:
        first_hand()
        print(f"Your cards is {player_card} and your score is {playerscore}\nDealer's first hand is {dealer_card[0]}")
        if playerscore == 21:
            playagain = input(f"You have blackjack! Do you want to play again? y/n ")
            endgame = yes_or_no(playagain)
        else:
            hit_or_stand = "h"
            while hit_or_stand == "h":
                hit_or_stand = input(f"Please hit for 'h' and stand for 's'. ")
                if hit_or_stand == "h":
                    hit_for_player()
                    playerscore = sum(player_card)
                    print(f"Your cards is {player_card} and your score is {playerscore}\nDealer's first hand is {dealer_card[0]}")
                    if playerscore > 21:
                        playagain = input("You lose! Do you want to play again? y/n ")
                        endgame = yes_or_no(playagain)
                        hit_or_stand = "a"
                    elif playerscore == 21:
                        playagain = input("You won! Do you want to play again? y/n ")
                        endgame = yes_or_no(playagain)
                        hit_or_stand = "a"


            if hit_or_stand == "s":
                while dealerscore < 17:
                    hit_for_dealer()
                    dealerscore = sum(dealer_card)
                if dealerscore > 21:
                    print(f"Your total score is {playerscore} and dealer's {dealerscore}.")
                    playagain = input(f"You won! Do you want to play again? y/n ")
                    endgame = yes_or_no(playagain)
                elif dealerscore < 21:
                    if dealerscore > playerscore:
                        print(f"Your total score is {playerscore} and dealer's {dealerscore}.")
                        playagain = input(f"You lose! Do you want to play again? y/n ")
                        endgame = yes_or_no(playagain)
                    elif dealerscore == playerscore:
                        print(f"Your total score is {playerscore} and dealer's {dealerscore}.")
                        playagain = input(f"Draw! Do you want to play again? y/n ")
                        endgame = yes_or_no(playagain)
                    else:
                        print(f"Your total score is {playerscore} and dealer's {dealerscore}.")
                        playagain = input(f"You won! Do you want to play again? y/n ")
                        endgame = yes_or_no(playagain)














































