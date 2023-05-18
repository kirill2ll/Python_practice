from collections import deque

chocolate = deque([int(num) for num in input().split(", ")])
milk = deque([int(num) for num in input().split(", ")])

number_of_shakes = 0

while number_of_shakes < 5 and len(chocolate) > 0 and len(milk) > 0:
    current_milk = milk.popleft()
    current_choco = chocolate.pop()
    if current_choco <= 0 and current_milk <= 0:
        continue
    elif current_choco <= 0:
        milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolate.append(current_choco)
        continue

    if current_choco == current_milk:
        number_of_shakes += 1
    else:
        milk.append(current_milk)
        chocolate.append(current_choco - 5)

if number_of_shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(num) for num in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(num) for num in milk]) if milk else 'empty'}")
