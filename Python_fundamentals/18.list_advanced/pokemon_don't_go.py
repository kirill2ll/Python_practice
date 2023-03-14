# Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression. And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those closest to you naturally get further, and those further from you, get closer.
# You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
# When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
# You must increase the value of all elements in the sequence which are less or equal to the removed element with the value of the removed element.
# You must decrease the value of all elements in the sequence which are greater than the removed element with the value of the removed element.
# If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
# If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
# The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
# The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).

def increase_decrease_func(number, input_list):
    for i in range (len(input_list)):
        if input_list[i] <= number:
            input_list[i] += number
        else:
            input_list[i] -= number

    return input_list

input_list = list(map(int, input().split(" ")))
sum_of_removed_elements = 0

while len(input_list) != 0:
    index = int(input())

    if index < 0:
        last_element = input_list[-1]
        removed_element = input_list[0]
        input_list[0] = last_element

    elif index >= len(input_list):
        first_element = input_list[0]
        removed_element = input_list[-1]
        input_list[-1] = first_element

    else:
        removed_element = input_list.pop(index)

    sum_of_removed_elements += removed_element
    input_list = increase_decrease_func(removed_element, input_list)

print(sum_of_removed_elements)

