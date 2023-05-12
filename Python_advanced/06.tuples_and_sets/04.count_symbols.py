# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.



input_line = input()

repeats = {}

for ch in input_line:
    if ch not in repeats:
        repeats[ch] = 0
    repeats[ch] += 1

[print(f"{key}: {value} time/s") for key, value in sorted(repeats.items())]