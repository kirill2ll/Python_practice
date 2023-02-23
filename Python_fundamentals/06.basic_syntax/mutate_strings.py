# You will be given two strings. Transform the first string into the second one, letter by letter, starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.


first_string = input()
second_string = input()
previous_string = first_string
for ch in range(len(first_string)):
    left_part = second_string[0:ch+1]
    right_part = first_string[ch+1:len(first_string)]
    current_string = left_part + right_part
    if (current_string != previous_string):
        previous_string = current_string
        print(current_string)