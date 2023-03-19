def return_hidden_number(number):
    list_to_return = []
    int_num = int(number)
    for num in number:
        if int(num) != 0:
            if int_num % int(num) == 0:
                list_to_return.append(num)

    return int("".join(list_to_return))


first_player = input()
second_player = input()

first_result = return_hidden_number(first_player)
second_result = return_hidden_number(second_player)


if first_result > second_result:
    print(f"Ronnie {first_result}")
elif first_result < second_result:
    print(f"Reanne {second_result}")
else:
    print(f"Tie {first_result}")



