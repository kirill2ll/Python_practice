number_of_clients = int(input())
total_bill = 0

for client in range(number_of_clients):

    client_bill = 0
    client_items = 00

    while True:
        order = input()

        if order == "Finish":
            break
        elif order == "basket":
            client_bill += 1.5
        elif order == "wreath":
            client_bill += 3.8
        elif order == "chocolate bunny":
            client_bill += 7

        client_items += 1

    if client_items % 2 == 0:
        client_bill = client_bill * 0.8

    total_bill += client_bill

    print(f"You purchased {client_items} items for {client_bill:.2f} leva.")

print(f"Average bill per client is: {total_bill/number_of_clients:.2f} leva.")

