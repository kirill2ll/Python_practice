# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
#
# · Opening bracket – "(",
#
# · Closing bracket – ")" or
#
# · Random string
#
# Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.


number_of_lines = int(input())
balanced = False
open = False  #checking if the brackets are open

for i in range(number_of_lines):
    line = input()
    if line == "(" and not open:
        open = True
        balanced = False
    elif line == ")" and open:
        open = False
        balanced = True
    elif line == "(" and open:
        balanced = False
        break
    elif line == ")" and not open:
        balanced = False
        break

print("BALANCED") if balanced else print("UNBALANCED")

