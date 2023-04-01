# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.
#


line = input().upper()

#the output text
final_string = ""

#creating temporary string that will be duplicated several time A3 => AAA
current_string_to_repeat = ""

#creating a string for the digit after the symbols that should be repeated A10 => AAAAAAAAAA
current_digit_string = ""

# count of unique symbols
unique_symbols = 0

for i in range(len(line)):
    ch = line[i]

    if ch.isdigit(): #when ch is a digit
        #adding symbol to the digit string e.g. 1 + 3 + 2 => 132
        current_digit_string += ch

        #checking if it's not the last symbol of our main string to avoid out of range
        if i == len(line) - 1:
            final_string += current_string_to_repeat * int(current_digit_string)
        #checking if the next symbol is a digit and adding continue so we can keep adding digits 1 + 3 + 2 => 132
        elif line[i + 1].isdigit():
            continue
        #adding symbols to the output string by multiplying it with the digit
        else:
            final_string += current_string_to_repeat * int(current_digit_string)
            #resetting
            current_string_to_repeat = ""
            current_digit_string = ""

    else:  # when ch is a letter or symbol eg @ # etc
        current_string_to_repeat += ch
        if ch not in final_string:
            unique_symbols += 1


print(f"Unique symbols used: {unique_symbols} \n{final_string}")

# https://softuni.bg/forum/43347/python-fundamentals-text-processing-rage-quit
