# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:
# merge {startIndex} {endIndex}
# divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.

# functions
def merge_func(command_line, words):
    commands = command_line.split(" ")
    command = commands[0]
    start_index = int(commands[1])
    end_index = int(commands[2])

    # check for indexes out of the list
    if end_index >= len(words):
        end_index = len(words) - 1

    output_list = []
    merge_word = ""

    for i in range(len(words)):
        if start_index <= i <= end_index:
            merge_word += words[i]
            if i == end_index:
                output_list.append(merge_word)
        else:
            output_list.append(words[i])

    return output_list


def divide_the_word(word, number_of_parts):
    output_list = []
    word_to_list = list(word)
    word_index = 0

    for i in range(number_of_parts):
        number_of_letters = len(word) // number_of_parts

        current_word = ""
        if i == number_of_parts - 1:
            current_word = word[word_index::]
        else:
            while number_of_letters != 0:
                current_word += str(word_to_list[word_index])

                number_of_letters -= 1
                word_index += 1

        output_list.append(current_word)

    return output_list


def divide_func(command_line, words):
    commands = command_line.split(" ")
    command = commands[0]
    index = int(commands[1])
    partitions = int(commands[2])

    output_list = []
    for i in range(len(words)):
        if i == index:
            output_list += divide_the_word(words[i], partitions)
        else:
            output_list.append(words[i])

    return output_list


# input
words = input().split(" ")

while True:
    command_line = input()

    if command_line == "3:1":
        break

    if "merge" in command_line:
        words = merge_func(command_line, words)
    elif "divide" in command_line:
        words = divide_func(command_line, words)

print(" ".join(words))
