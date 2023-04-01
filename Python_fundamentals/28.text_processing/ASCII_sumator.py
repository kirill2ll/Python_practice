# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On each of the first two lines, you will receive a single character. On the last line, you get a random string. Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.



ch1 = ord(input())
ch2 = ord(input())

text = input()
output_sum = 0

for current_ch in text:
    current_ord = ord(current_ch)
    if ch1 < current_ord < ch2:
        output_sum += current_ord

print(output_sum)