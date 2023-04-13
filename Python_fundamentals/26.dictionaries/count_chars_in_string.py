# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"


text = input().replace(" ", "")
output_dict = {}

for ch in text:
    if ch not in output_dict.keys():
        output_dict[ch] = 0
    output_dict[ch] += 1
    #print(output_dict)

for char, occurrences in output_dict.items():
    print(f"{char} -> {occurrences}")