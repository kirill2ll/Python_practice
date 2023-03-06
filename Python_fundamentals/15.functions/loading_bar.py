# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without
# remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received
# in the input. Print the result on the console.
# For more clarification, see the examples below.


def loading_bar(percentage):
    if percentage == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{percentage}% [{percentage//10*'%'}{(10-percentage//10)*'.'}]")
        print("Still loading...")

percantage = int(input())
loading_bar(percantage)
