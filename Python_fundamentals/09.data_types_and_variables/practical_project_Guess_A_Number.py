# We will make the console game "Guess A Number".
# "Guess A Number" is a game in which your opponent, "the computer", chooses a random number between "1 and 100", and your task is to guess this number.
# After each number you enter, the computer will give you a hint of whether the number is greater or less than the number you selected until you guess the correct number
import random

computer_number = random.randint(1, 100)
guessed = False
counter = 0

while guessed != True:
    my_number = int(input())
    counter += 1
    if my_number == computer_number:
        guessed = True
        break

    if my_number > computer_number:
        print("The number is smaller")
    else:
        print("The number is bigger")

if (guessed):
    print(f"Well done, you guessed from the {counter} try, the computer number was {computer_number}")
