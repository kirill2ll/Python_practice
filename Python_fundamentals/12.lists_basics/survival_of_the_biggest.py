# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".


input_numbers = input().split(" ")
numbers_to_remove = int(input())

list_of_number = []

# string list of numbers to int list
for num in input_numbers:
    list_of_number.append(int(num))

for _ in range(numbers_to_remove):
    smallest_number = min(list_of_number)
    list_of_number.remove(smallest_number)

for i in range(len(list_of_number)):
    if i != (len(list_of_number) - 1):
        print(list_of_number[i], end=", ")
    else:
        print(list_of_number[i])
