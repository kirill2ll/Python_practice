# You will be given the coordinates of four points.
# The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to the center of the coordinate system (0, 0).
# You can reuse the method that you wrote for the previous problem.
# If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lower integer
import math


def find_distance_from_center(x, y):
    hypotenuse_square = x * x + y * y
    return math.sqrt(hypotenuse_square)


# creating the function to which will prepare the coordinates for find_distance_from_center
def find_distance_between_points(x1, y1, x2, y2):
    return find_distance_from_center(abs(x1 - x2), abs(y1 - y2))


# function to find the closest point and print it on console
def print_line_starting_center_closest_point(x1, y1, x2, y2):
    first_point = find_distance_from_center(x1, y1)
    second_point = find_distance_from_center(x2, y2)
    closest_x, closest_y, farthest_x, farthest_y = None, None, None, None
    if first_point < second_point:
        closest_x = x1
        closest_y = y1
        farthest_x = x2
        farthest_y = y2
    else:
        closest_x = x2
        closest_y = y2
        farthest_x = x1
        farthest_y = y1

    print(f"({int(closest_x)}, {int(closest_y)})({int(farthest_x)}, {int(farthest_y)})")



x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

first_line = find_distance_between_points(x1, y1, x2, y2)
second_line = find_distance_between_points(x3, y3, x4, y4)

if first_line >= second_line:
    print_line_starting_center_closest_point(x1, y1, x2, y2)
else:
    print_line_starting_center_closest_point(x3, y3, x4, y4)
