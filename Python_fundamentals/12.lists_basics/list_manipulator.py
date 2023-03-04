# The list may be manipulated by one of the following current_lines:
# "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
# If the index is outside the boundaries of the list, print "Invalid index"
# A negative index is considered invalid
# "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
# If there are two or more equal min/max elements, return the index of the rightmost one
# If a min/max even/odd element cannot be found, print "No matches"
# "first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# "last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
# If the count is greater than the list length, print "Invalid count"
# If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
# "end" - stop taking input and print the final state of the list
import sys

input_list = input().split(" ")
list_int = []

for el in input_list:
    list_int.append(int(el))

current_line = input()

while current_line != "end":

    current_line_list = current_line.split(" ")
    command = current_line_list[0]

    if command == "exchange":
        index = int(current_line_list[1])
        if 0 <= index < len(list_int):
            left_part = list_int[:index + 1]
            right_part = list_int[index + 1::]
            list_int = right_part + left_part

        else:
            print("Invalid index")
    elif command == "max":
        odd_or_even = current_line_list[1]
        current_max = -sys.maxsize
        max_index = -1
        if odd_or_even == "even":
            for i in range(len(list_int)):
                el = list_int[i]
                if (el % 2 == 0) and el >= current_max:
                    current_max = el
                    max_index = i

        else:
            for i in range(len(list_int)):
                el = list_int[i]
                if (el % 2 != 0) and el >= current_max:
                    current_max = el
                    max_index = i
        if max_index > -1:
            print(max_index)
        else:
            print("No matches")

    elif command == "min":
        odd_or_even = current_line_list[1]
        current_min = sys.maxsize
        max_index = -1
        if odd_or_even == "even":
            for i in range(len(list_int)):
                el = list_int[i]
                if (el % 2 == 0) and el <= current_min:
                    current_min = el
                    max_index = i

        else:
            for i in range(len(list_int)):
                el = list_int[i]
                if (el % 2 != 0) and el <= current_min:
                    current_min = el
                    max_index = i
        if max_index > -1:
            print(max_index)
        else:
            print("No matches")

    elif command == "first":
        count = int(current_line_list[1])
        odd_or_even = current_line_list[2]
        list_to_return = []
        if count > len(list_int):
            print("Invalid count")
        else:
            if odd_or_even == "even":
                for el in list_int:
                    if el % 2 == 0:
                        list_to_return.append(el)
                        count -= 1

                    if count == 0:
                        break
            else:
                for el in list_int:
                    if el % 2 != 0:
                        list_to_return.append(el)
                        count -= 1

                    if count == 0:
                        break

            print(list_to_return)

    elif command == "last":
        count = int(current_line_list[1])
        odd_or_even = current_line_list[2]
        list_to_return = []
        if count > len(list_int):
            print("Invalid count")
        else:
            if odd_or_even == "even":
                for i in range(len(list_int) - 1, -1, -1):
                    if list_int[i] % 2 == 0:
                        list_to_return.append(list_int[i])
                        count -= 1

                    if count == 0:
                        break
            else:
                for i in range(len(list_int) - 1, -1, -1):
                    if list_int[i] % 2 != 0:
                        list_to_return.append(list_int[i])
                        count -= 1

                    if count == 0:
                        break

            list_to_return.reverse()
            print(list_to_return)
            # reverse_list = list_to_return.sort(reverse=True)
            # print(list_to_return.sort(reverse=True))
            # print(reverse_list)

    current_line = input()


print(list_int)