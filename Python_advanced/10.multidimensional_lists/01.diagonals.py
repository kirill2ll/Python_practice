lines = int(input())

matrix = [[int(num) for num in input().split(", ")] for line in range(lines)]

primary_diagonal = [matrix[i][i] for i in range(lines)]
secondary_diagonal = [matrix[i][lines - 1 - i] for i in range(lines)]
print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
