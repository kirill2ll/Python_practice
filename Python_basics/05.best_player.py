best_player = None
best_score = -1

while True:
    current_player = input()

    if current_player == "END":
        break

    number_goals = int(input())

    if number_goals > best_score:
        best_player = current_player
        best_score = number_goals

    if number_goals >= 10:
        break

print(f"{best_player} is the best player!")

if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")
