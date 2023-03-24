# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze. On the following n lines, you will be given the maze itself. Here is a legend for the maze:
# "#" - means a wall; Kate cannot go through there
# " " - means empty space; Kate can go through there
# "k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
# If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
# Otherwise, print: "Kate cannot get out".

def next_position_is_valid(current_position, next_steps):
    if (current_position[0] + next_steps[0] < 0) \
            or (current_position[1] + next_steps[1] < 0) \
            or (current_position[0] + next_steps[0] >= len(matrix)) \
            or (current_position[1] + next_steps[1] >= len(matrix[0])):
        return False
    else:
        return True


def check_the_border(position_x, position_y, matrix):
    if position_x == 0 or position_x == len(matrix) - 1 or \
            position_y == 0 or position_y == len(matrix[0]) - 1:
        return True

    return False


lines = int(input())
matrix = []

#creating the matrix
for _ in range(lines):
    current_line = list(input())
    matrix.append(current_line)

# finding Kate
current_position = [0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "k":
            current_position = [i, j]

#the required steps to escape
count_steps = 0

#up right down left - the possible moves from the current position
next_positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

old_position = [0, 0]

keep_searching = True
not_found_exit = False
made_step = False

while keep_searching:
    made_step = False
    for i in range(len(next_positions)):
        next_steps = next_positions[i]
        if next_position_is_valid(current_position, next_steps):
            new_position_x = current_position[0] + next_steps[0]
            new_position_y = current_position[1] + next_steps[1]
            old_position_x = old_position[0]
            old_position_y = old_position[1]

            # making a step
            if (matrix[new_position_x][new_position_y] == " ") and \
                    (new_position_x != old_position_x or new_position_y != old_position_y):
                old_position = current_position
                current_position = [new_position_x, new_position_y]
                matrix[new_position_x][new_position_y] = "k"
                matrix[old_position[0]][old_position[1]] = " "
                count_steps += 1

                # checking the border and breaking the WHILE
                if check_the_border(new_position_x, new_position_y, matrix):
                    keep_searching = False
                    break

                # exit from FOR to start from the beginning
                made_step = True
                break

        # checked all steps and there is no exit or next move
        if (i == len(next_positions) - 1) and not made_step:
            keep_searching = False
            not_found_exit = True

# check if the current position is at the border adding the last step to escape
if check_the_border(current_position[0], current_position[1], matrix):
    count_steps += 1
    not_found_exit = False

#output
if not_found_exit:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {count_steps} moves")
