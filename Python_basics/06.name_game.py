best_name = None
best_result = 0

while True:
    name = input()

    if name == "Stop":
        break
    current_result = 0
    for i in range(len(name)):
        num = int(input())

        if num == ord(name[i]):
            current_result += 10
        else:
            current_result += 2

    if current_result >= best_result:
        best_name = name
        best_result = current_result

print(f"The winner is {best_name} with {best_result} points!")