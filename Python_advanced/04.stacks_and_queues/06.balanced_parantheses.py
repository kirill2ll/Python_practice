from collections import deque

input_line = input()
open_parentheses = deque()
open_list = "{[("
closed_list = ")]}"
is_balanced = True

for i in range(len(input_line)):
    current_parentheses = input_line[i]
    if current_parentheses in open_list:
        open_parentheses.append(current_parentheses)

    if (current_parentheses in closed_list) and (len(open_parentheses) <= 0):
        is_balanced = False
        break

    if (current_parentheses in closed_list) and (len(open_parentheses) > 0):
        current_open_parentheses = open_parentheses.pop()
        if ((current_parentheses == ")" and current_open_parentheses == "(")) or (
        (current_parentheses == "]" and current_open_parentheses == "[")) or (
        (current_parentheses == "}" and current_open_parentheses == "{")):
            continue
        else:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
