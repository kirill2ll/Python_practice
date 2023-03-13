# You will be given a number n representing the number of rows of the field. On the following n lines, you will receive each field row as a string with numbers separated by a space. Each number greater than zero represents a ship with health equal to the number value.
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1. If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.

#input
matrix_length = int(input())
matrix = []
for i in range(matrix_length):
    current_line = list(map(int, input().split(" ")))
    matrix.append(current_line)

attacks = list(input().split(" "))
destroyed_ships = 0

for i in range(len(attacks)):
    attack_coordinates = list(attacks[i].split("-"))
    x = int(attack_coordinates[0])
    y = int(attack_coordinates[1])
    matrix[x][y] -= 1
    if matrix[x][y] == 0:
        destroyed_ships += 1

print(destroyed_ships)

