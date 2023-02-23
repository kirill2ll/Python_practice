#Write a program that takes a single string and prints a list of all the capital letters indices.


str = input()

output = []

for ch in range(len(str)):
    if str[ch].isupper():
        output.append(ch)


print(output)

