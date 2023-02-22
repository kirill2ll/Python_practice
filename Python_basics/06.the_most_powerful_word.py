import math

word = input()
best_word = None
best_result = 0

while word != "End of words":
    current_result = 0
    for ch in word:
        current_result += ord(ch)

    first_letter = word[0].lower()
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u' or first_letter == 'y':
        current_result = current_result * len(word)
    else:
        current_result = math.floor(current_result / len(word))

    if current_result > best_result:
        best_word = word
        best_result = current_result

    word = input()

print(f"The most powerful word is {best_word} - {best_result}")