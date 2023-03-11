# Take/Skip Rope
# Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you should implement is as follows:
# Let us take the string "skipTest_String044160" as an example.
# Take every digit from the string and transfer it somewhere. After this operation, you should have two lists of items - a numbers list and a non-numbers list:
# Numbers' list: [0, 4, 4, 1, 6, 0]
# Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
# After that, take every digit in the numbers list and split it up into a take list and a skip list. In the take list, you should keep all digits at an even index. In the skip list, you should keep all digits at an odd index.
# Numbers' list: [0, 4, 4, 1, 6, 0]
# Take list: [0, 4, 6]
# Skip list: [4, 1, 0]
# Afterward, iterate over both lists:
# First, take m characters from the non-numbers list and store it in a result string
# Then, skip n characters from the non-numbers list
# Note that the skipped characters are summed up as they go. The process would look like this:
# Current string: "skipTest_String". Take 0 characters and skip 4 characters:
# Taken string: ""
# Skipped string: "skip"
# The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
# Taken string: "Test"
# Skipped string: "_"
# The string looks like this: "String". Take 6 characters and skip 0 characters:
# Taken string: "String"
# Skipped string: ""
# The final string is "TestString".
# After that, print the final string on the console.

#functions
def find_string(take_index, skip_index, list_to_string):

    take_string = list_to_string[:take_index]
    left_string = list_to_string[take_index+skip_index:]

    return take_string, left_string


#input
input_list = list(input())

number_list = [int(num) for num in input_list if num.isnumeric()]
letter_list = [letter for letter in input_list if not letter.isnumeric()]

#filtering number list
take_list = []
skip_list = []

for i in range(len(number_list)):
    if i % 2 == 0:
        take_list.append(number_list[i])
    else:
        skip_list.append(number_list[i])


final_list = []
letter_list_to_string = "".join(letter_list)

for i in range(len(take_list)):
    result_str_to_append, letter_list_to_string = find_string(take_list[i], skip_list[i], letter_list_to_string)
    final_list.append(result_str_to_append)

print("".join(final_list))