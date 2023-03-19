allowed_letters = input().split(",")
number_to_check = int(input())

def check_letters(ch, letters):
    return ch in letters

is_valid = True

for i in range(number_to_check):
    current_plate = list(input())

    index_letters = [0, 1, 6, 7]

    for index in range(len(current_plate)):
        if index in index_letters:
            is_valid = check_letters(current_plate[index], allowed_letters)
        else:
            is_valid = current_plate[index].isnumeric()
        if not is_valid:
            break

    # for index in range(len(index_letters)):
    #     index_value = index_letters[index]
    #     is_valid = check_letters(current_plate[index_value], allowed_letters)
    #
    #     if not is_valid:
    #         break


    if is_valid:
        print("".join(current_plate))
