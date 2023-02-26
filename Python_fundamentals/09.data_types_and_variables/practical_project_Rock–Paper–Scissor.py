# Rock-Paper-Scissors is a simple two-player game, where you and your opponent (the computer) simultaneously choose one of the following three options: "rock", "paper", or "scissors".
# The rules are as follows:
#
# · Rock beats scissors (the scissors get broken by the rock)
#
# · Scissors beats paper (the paper gets cut by the scissors)
#
# · Paper beats rock (the paper covers the rock)
#
# The winner is the player whose choice beats the choice of his opponent.
# If both players choose the same option (e.g., "paper"), the game outcome is "draw".
import random

user_input = input().lower()

list_of_options = ["rock", "paper", "scissors", "r", "p", "s"]
computer_list_of_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_list_of_options)

draw = False
user_wins = False

if user_input in list_of_options:
    if (user_input == "rock" or user_input == "r") and computer_choice == "scissors":
        user_wins = True
    elif (user_input == "paper" or user_input == "p") and computer_choice == "rock":
        user_wins = True
    elif (user_input == "scissors" or user_input == "s") and computer_choice == "paper":
        user_wins = True
    elif user_input[0] == computer_choice[0]:
        draw = True

    # output

    if draw:
        print("Draw", end=" ")
    elif user_wins:
        print("User wins", end=" ")
    else:
        print("Computer wins", end=" ")

    print(f"because computer selected {computer_choice}")

else:
    print("Wrong input")

