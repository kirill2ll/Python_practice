# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.

input_list = input().split(", ")

#finding the number of times zero is found in the list
number_of_zeroes = input_list.count("0")

#string list to int list
for i in range(len(input_list)):
    input_list[i] = int(input_list[i])

#removing zeroes and adding at the end
for i in range(number_of_zeroes):
    input_list.remove(0)
    input_list.append(0)

print(input_list)