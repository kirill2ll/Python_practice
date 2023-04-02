# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.


import re

pattern = r"\d+"


while True:
    line = input()

    if len(line) == 0:
       break

    result = re.findall(pattern, line)
    if len(result) > 0:
        print(" ".join(result), end=" ")