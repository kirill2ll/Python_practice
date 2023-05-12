number_of_lines = int(input())

longest_intersection = []

for _ in range(number_of_lines):
    data_list = [[int(parts) for parts in parts.split(",")] for parts in input().split("-")]

    current_intersection = {numbers for numbers in range(data_list[0][0], data_list[0][1] + 1)} & \
                           {numbers for numbers in range(data_list[1][0], data_list[1][1] + 1)}
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {[*longest_intersection]} with length {(len(longest_intersection))}")
