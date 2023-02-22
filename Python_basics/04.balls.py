import math

number_balls = int(input())
total_points = 0
red_balls, orange_balls, yellow_balls, white_balls, other_balls, black_balls = 0, 0, 0, 0, 0, 0

for _ in range(number_balls):
    current_ball = input()

    if current_ball == "red":
        total_points += 5
        red_balls += 1
    elif current_ball == "orange":
        total_points += 10
        orange_balls += 1
    elif current_ball == "yellow":
        total_points += 15
        yellow_balls += 1
    elif current_ball == "white":
        total_points += 20
        white_balls += 1
    elif current_ball == "black":
        total_points = math.floor(total_points / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
