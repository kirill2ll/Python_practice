# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.
#


line = input().upper()

final_string = ""

current_string_to_repeat = ""

#count of unique symbols
unique_symbols = 0

for ch in line:
    if ch.isdigit():
        final_string += current_string_to_repeat * int(ch)
        current_string_to_repeat = ""

    else: #when ch is a letter or symbol eg @ # etc
        current_string_to_repeat += ch
        if ch not in final_string:
            unique_symbols += 1


# def count_unique_symbols(my_text):
#     unique_symbols = ""
#     unique_symbols_count = 0
#
#     for ch in my_text:
#         if ch not in unique_symbols:
#             unique_symbols_count += 1
#             unique_symbols += ch
#
#     return unique_symbols_count


#symbols = count_unique_symbols(final_string)

print(f"Unique symbols used: {unique_symbols} \n{final_string}")
