from collections import deque

number_of_stations = int(input())
gas_q = deque()
distance_q = deque()

for _ in range(number_of_stations):
    line = list(map(int, input().split()))
    gas_q.append(line[0])
    distance_q.append((line[1]))


is_Found = False
station_to_start = 0

while not is_Found:
    current_gas = 0
    current_distance = 0
    for i in range(number_of_stations):
        current_gas += gas_q[i]
        current_distance = distance_q[i]

        current_gas -= current_distance
        if current_gas < 0:
            station_to_start += 1
            #switch the 1st station to the end
            gas_q.append(gas_q.popleft())
            distance_q.append(distance_q.popleft())
            break
        if i == number_of_stations - 1:
            is_Found = True


print(station_to_start)


