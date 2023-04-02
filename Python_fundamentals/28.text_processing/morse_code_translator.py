# Write a program that translates messages from Morse code to English (capital letters). Use this page to help you (without the numbers). The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


#dict to lists to access keys
letter_list = list(MORSE_CODE_DICT.keys())

symbols_list = list(MORSE_CODE_DICT.values())
to_decode_message = input().split("|")
output_message = []

for words in to_decode_message:

    list_of_word = words.split()
    current_string = ""
    for word in list_of_word:
        index = symbols_list.index(word)
        current_string+= letter_list[index]

    output_message.append(current_string)


print(" ".join(output_message))
