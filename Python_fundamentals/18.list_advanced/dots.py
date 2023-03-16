# Dots
# You will be given a number n representing the number of rows of a board of dots and dashes. On the following n lines, you will receive each row of the board as a string with symbols (dots and dashes only), separated by a single space.
# Your task is to find and print the largest count of dots that could be connected at once. You could only connect horizontally or vertically.


# to escape the error out of index, will add additional PERIMETER wall
def add_additional_wall(matrix):
    matrix.insert(0, ["-"] * (len(matrix[0]) + 2))
    matrix.insert(len(matrix), ["-"] * (len(matrix[0])))

    for i in range(1, len(matrix) - 1):
        matrix[i].insert(0, "-")
        matrix[i].insert(len(matrix[i]), "-")

    return matrix


# function to find potential moves
def check_possible_moves(x, y, matrix):
    possible_positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for position in possible_positions:
        new_x = x + position[0]
        new_y = y + position[1]
        if matrix[new_x][new_y] == "." and \
                [new_x, new_y] not in was_here and \
                [new_x, new_y] not in queue:
            queue.append([new_x, new_y])

    return queue


# function to start the process for every dot:
def start_process_for_dot(x, y, matrix):
    was_here.clear()
    current_result = 0

    while True:
        queue = check_possible_moves(x, y, matrix)

        # adding the dot to the visited dots
        was_here.append([x, y])

        current_result += 1

        if len(queue) == 0: #if the queue is empty break WHILE
            break
        else:
            removed_dot = queue.pop(0) #taking a dot from the queue
            x = removed_dot[0]
            y = removed_dot[1]

    return current_result

#visited dots
was_here = []

#next moves
queue = []

matrix = []
best_result = 0
current_result = 0

# input
number_of_lines = int(input())
for i in range(number_of_lines):
    line = input().split(" ")
    matrix.append(line)

matrix = add_additional_wall(matrix)

# check every dot and calculating the result of its connected dots
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):

        if matrix[i][j] == ".":
            current_result = start_process_for_dot(i, j, matrix)
            if current_result > best_result:
                best_result = current_result

print(best_result)
