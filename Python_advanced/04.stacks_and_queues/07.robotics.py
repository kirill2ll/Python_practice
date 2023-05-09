import datetime
from collections import deque

robot_input_line = input().split(";")
robots = deque()
for i in range(len(robot_input_line)):
    robot_line = robot_input_line[i].split("-")
    robot = {
        "name": robot_line[0],
        "default_time": int(robot_line[1]) + 1,
        "current_time": 0
    }
    robots.append(robot)

time = datetime.datetime.strptime(input(), "%H:%M:%S")

products = deque()

product = input()

while product != "End":
    products.append(product)
    product = input()

while len(products) != 0:
    time += datetime.timedelta(0, 1)

    #increate current time
    for robot in robots:
        if robot["current_time"] != 0:
            robot["current_time"] += 1

        if robot["current_time"] == robot["default_time"]:
            robot["current_time"] = 0

    #find the free robot
    free_robot = {}
    is_free = False
    for robot in robots:
        if robot["current_time"] == 0:
            is_free = True
            free_robot = robot
            robot["current_time"] = 1
            break

    #printing the results if the robot is ready
    if is_free:
        print(f'{robot["name"]} - {products.popleft()} [{time.strftime("%H:%M:%S")}]')
    else:
        products.append(products.popleft())




