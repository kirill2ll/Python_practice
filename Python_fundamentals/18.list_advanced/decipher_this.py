# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)

def find_character_code(word):
    character_code = []
    rest_of_word = []

    for i in range(len(word)):
        ch = word[i]
        if ch.isnumeric():
            character_code.append(ch)
        else:
            rest_of_word.append(ch)

    return int("".join(character_code)), rest_of_word

list_words = input().split(" ")
output_list = []

for word in list_words:
    current_word = []
    ch, rest_of_word = find_character_code(word)
    current_word.append(chr(ch))
    current_word += rest_of_word
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    output_list.append("".join(current_word))

#printing
print(" ".join(output_list))
