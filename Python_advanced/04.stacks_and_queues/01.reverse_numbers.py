#Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack. Print the reversed integers on one line, separated by a single space.


numbers = list(map(int, input().split()));
new_stack = []
for i in range(len(numbers)):
    switch_num = numbers.pop()
    new_stack.append(switch_num)

print(*new_stack)