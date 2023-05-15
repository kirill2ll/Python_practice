# First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.



first_set = { int(num) for num in input().split()}
second_set = {int(num) for num in input().split()}

commands = {
    "Add First": lambda x: [first_set.add(el) for el in x],
    "Add Second": lambda x: [second_set.add(el) for el in x],
    "Remove First": lambda x: [first_set.discard(el) for el in x],
    "Remove Second": lambda x: [second_set.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first_set.issubset(second_set) or second_set.issubset(first_set) else print(False)
}

for _ in range(int(input())):
    current_input = input().split()
    current_command = f"{current_input[0]} {current_input[1]}"

    if len(current_input) > 2:
        array = [int(num) for num in current_input[2::]]
        commands[current_command](array)
    else:
        commands[current_command]()


print(", ".join([str(num) for num in sorted(first_set)]))
print(", ".join([str(num) for num in sorted(second_set)]))
