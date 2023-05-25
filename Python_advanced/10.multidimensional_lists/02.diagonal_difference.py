lines = int(input())

matrix = [[int(num) for num in input().split()] for line in range(lines)]

primary_diagonal = [matrix[i][i] for i in range(lines)]
secondary_diagonal = [matrix[i][lines - 1 - i] for i in range(lines)]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)