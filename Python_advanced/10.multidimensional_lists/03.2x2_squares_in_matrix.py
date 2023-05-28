rows, cols = [int(num) for num in input().split()]

matrix = [input().split() for _ in range(rows)]
count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col+1] and matrix[row][col] == matrix[row+1][col+1] and matrix[row][col] == matrix[row+1][col]:
            count += 1

print(count)