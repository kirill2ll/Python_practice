# On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the first sequence.
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). When you find a char, you should add it to the message and remove it from the string. It means that for the following index, the text will contain one character less.
# Print the final message.


sequence_of_number = input().split(" ")
message = list(input())
output_list = []

for element in sequence_of_number:
    #finding index in the element using sum
    index = 0
    for i in range(len(element)):
        index += int(element[i])

    #removing index which is greater than the lenght of the message
    while (index >= len(message)):
        index -= len(message)

    output_list.append(message[index])
    del message[index]

print("".join(output_list))


