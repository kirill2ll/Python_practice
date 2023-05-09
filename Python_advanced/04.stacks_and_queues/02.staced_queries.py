# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.


number_of_lines = int(input())
stack = []

for _ in range(number_of_lines):
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if len(stack) > 0:
            stack.pop()
    elif command[0] == 3:
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == 4:
        if len(stack) > 0:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")


