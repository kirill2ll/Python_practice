n = int(input())                             # read n, the number of rows
board = [input().split() for _ in range(n)]  # read n rows of dots and dashes

def count_dots(start_x, start_y):
    if not (0 <= start_x < n and 0 <= start_y < n) or board[start_y][start_x] != ".": # base case
        return 0
    board[start_y][start_x] = "-"

    # Recursively count dots in all four directions
    total_dots = 1  # include the current dot in the count
    total_dots += count_dots(start_x + 1, start_y)  # right
    total_dots += count_dots(start_x - 1, start_y)  # left
    total_dots += count_dots(start_x, start_y + 1)  # down
    total_dots += count_dots(start_x, start_y - 1)  # up

    return total_dots

max_dots = 0
for y in range(n):
    for x in range(n):
        if board[y][x] == ".":
            dots_count = count_dots(x, y)
            if dots_count > max_dots:
                max_dots = dots_count

print(max_dots)