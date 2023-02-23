#You will be given a number. Print the largest number that can be formed from the digits of the given numbe

number = input()
number_list_str = list(number) #creating a string array ["1", "2", "3"]

number_list_int = [int(num_to_str) for num_to_str in number_list_str] #converting string array to int array [1, 2, 3]

number_list_int.sort(reverse=True) #sorting the array [3, 2, 1]

for num in number_list_int:
    print(num, end="") #printing the array


# my_list = [7, 6, 4, 5]
# print(my_list.sort())
#
# scores = [5, 7, 4, 6, 9, 8]
# scores.sort()
#
# print(scores)
