# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def check_for_palindrome(numbers):
    palindrome_true_false_list = []
    for num in numbers:
        if num == num[::-1]:
            palindrome_true_false_list.append(True)
        else:
            palindrome_true_false_list.append(False)
    return palindrome_true_false_list


numbers_list = input().split(", ")

output_list = check_for_palindrome(numbers_list)
for el in output_list:
    print(el)

