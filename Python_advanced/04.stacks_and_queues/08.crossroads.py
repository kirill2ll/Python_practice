from collections import deque

green = int(input())
yellow = int(input())

command = input()
cars_q = deque()
cars_count = 0
has_crashed = False

while command != 'END' and not has_crashed:

    if command == "green":
        current_green = green
        while len(cars_q) > 0 and current_green > 0:
            current_car = cars_q.popleft()
            cars_count+=1
            current_green -= len(current_car)

            if current_green < 0:
                if current_green + yellow < 0:
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[current_green + yellow]}.")
                    has_crashed = True
                    break
                else:   #break, because we already used the yellow color
                    break

    else: #adding the car to the queue
        cars_q.append(command)


    command = input()

if not has_crashed:
    print("Everyone is safe.")
    print(f"{cars_count} total cars passed the crossroads.")