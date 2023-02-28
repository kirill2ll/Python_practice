# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# "OutOfStock {gift}"
# Find the gifts with this name in your collection, if any, and change their values to "None".
# "Required {gift} {index}"
# If the index is valid, replace the gift on the given index with the given gift.
# "JustInCase {gift}"
# Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"



all_gifts = input().split(" ")

current_line = input()

while current_line != "No Money":
    list_line = current_line.split(" ")
    command = list_line[0]

    gift = list_line[1]

    if command == "OutOfStock":
        for i in range(len(all_gifts)):
            if all_gifts[i] == gift:
                all_gifts[i] = "None"
    elif command == "JustInCase":
        all_gifts[-1] = gift
    elif command == "Required":
        current_index = int(list_line[2])
        if 0 <= current_index < len(all_gifts):
            all_gifts[current_index] = gift

    current_line = input()

#printing
for gift in all_gifts:
    if gift != "None":
        print(gift, end= " ")
