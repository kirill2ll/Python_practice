# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# 0 - empty space
# 1 - first player move
# 2 - second player move

matrix = []
have_winner = False
winner = ""

for _ in range(3):
    line = input().split(" ")
    matrix.append(line)

for i in range(3):
    #vertical check
    if matrix[i][0] == matrix[i][1] == matrix[i][2]:
        have_winner = True
        winner = matrix[i][0]

    #horizontal check
    if matrix[0][i] == matrix[1][i] == matrix[2][i]:
        have_winner = True
        winner = matrix[0][i]


#diagonal check
if (matrix[0][0] == matrix[1][1] == matrix[2][2]) or\
        (matrix[0][2] == matrix[1][1] == matrix[2][0]):
    have_winner = True
    winner = matrix[1][1]

if have_winner and (winner == "1" or winner == "2"):
    if winner == "1":
        print(f"First player won")
    if winner == "2":
        print(f"Second player won")
else:
    print("Draw!")
