################################################################
#Function
#Name: Random_choice
#Purpose: It randomly chooses the computer's hand
#Arguements in: None
#Returned Values: String of random_choice
################################################################


################################################################
#Function Name: Get_User_Choice
#Purpose: User chooses their hand 1, 2, or 3
#Arguements in: None
#Returned Values: String of player's choice
################################################################


###############################################################################
## Function print_hand(computr_hand,player_hand)
## Purpose          : The function prints the computer's and the player's
##                    choices of hand
## Arguements in    : computer_hadnd and player_hand as strings.
## Returned values  : NONE
###############################################################################
import random

def Random_choice():
    choice = random.randint(1,3)
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Scissors"
    else:
        return "Paper"

def Get_User_Choice():
    print("""
Welcome to Rock-Paper-Scissors!
Enter your choice:

        1. Rock
        2. Scissors
        3. Paper

""")

    player_choice = input("1, 2 or 3: ")

    if player_choice == "1":
        return "Rock"
    elif player_choice == "2":
        return "Scissors"
    elif player_choice == "3":
        return "Paper"

def print_hand(player_hand, computer_hand):
    
    print("The choices are in")
    print("I chose", computer_hand)
    print("You chose", player_hand)

def computer_wins(computer_hand, player_hand):
    if computer_hand == "Rock" and player_hand == "Scissors":
        return True
    if computer_hand == "Paper" and player_hand == "Rock":
        return True
    if computer_hand == "Scissors" and player_hand == "Paper":
        return True
    else:
        return False

def player_wins(computer_hand, player_hand):
    if player_hand == "Rock" and computer_hand == "Scissors":
        return True
    if player_hand == "Paper" and computer_hand == "Rock":
        return True
    if player_hand == "Scissors" and computer_hand == "Paper":
        return True
    else:
        return False

def print_winner(computer_hand, player_hand, remlives):
    if computer_wins(computer_hand, player_hand):
        print("You lost. I win")
    elif player_wins(computer_hand, player_hand):
        print("You won. I lost")
    else:
        print("Draw")
    print("You have", remlives, "lives")

def main():
    lives = 5
    
    while lives >= 0:
        if lives == 0:
            print("You are dead.")
            print("Game over.")
            remlives = lives - 1
        else:
            computer_hand = Random_choice()
            player_hand = Get_User_Choice()

            if computer_wins(computer_hand, player_hand):
                remlives = lives - 1
            else:
                remlives = lives
            
            print_hand(player_hand, computer_hand)
            
            print_winner(computer_hand, player_hand, remlives)

        lives = remlives

main()

