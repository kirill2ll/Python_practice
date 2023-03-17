# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# The numbers 2, 8, 4, and 10 fall into the group of 10's.
# The numbers 13, 19, 14, and 15 fall into the group of 20's.

# function to return the ten's of a number. E.g. 25 => 3 (30's)
def return_ten_of_number(number):
    num_to_str = str(number)
    if len(num_to_str) == 1:
        return 1
    elif num_to_str == "100":   #special number 100!
        return 10
    elif num_to_str[1] == "0":
        return int(num_to_str[0])
    else:
        return int(num_to_str[0]) + 1

# function to create the length of the output list
def find_lenght_of_list(numbers):
    max_length = 0

    for num in numbers:
        current_length = return_ten_of_number(num)
        if current_length > max_length:
            max_length = current_length

    return max_length


def sort_tens(numbers):
    output_list = []
    output_list_len = find_lenght_of_list(numbers)
    #creating matrix for all tens [[10], [20], [30] etc]
    for lst in range(output_list_len + 1):
        output_list.append([])

    # adding numbers to the matrix
    for num in numbers:
        current_ten = return_ten_of_number(num)
        output_list[current_ten].append(num)

    #printing:
    for i in range(1, len(output_list)):
        print(f"Group of {i}0's: {output_list[i]}")


list_numbers = list(map(int, input().split(", ")))
sort_tens(list_numbers)
