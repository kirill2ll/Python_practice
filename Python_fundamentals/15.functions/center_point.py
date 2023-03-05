# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.
import math


def find_distance_from_center(x, y):
    hypotenuse_square = x*x + y*y
    return math.sqrt(hypotenuse_square)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance1 = find_distance_from_center(x1, y1)
distance2 = find_distance_from_center(x2, y2)

if distance1 < distance2:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")