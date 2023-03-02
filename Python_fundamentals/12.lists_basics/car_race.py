# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side. The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time).
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
#
#

input_list = input().split(" ")

half_of_list = len(input_list) // 2

right_half = input_list[len(input_list):half_of_list:-1]
left_half = input_list[:half_of_list:]

left_driver = 0
right_driver = 0

for i in range(len(left_half)):
    left_driver += int(left_half[i])
    right_driver += int(right_half[i])
    if left_half[i] == "0":
        left_driver *= 0.8
    if right_half[i] == "0":
        right_driver *= 0.8

side = "right"
winner = right_driver

if left_driver < right_driver:
    side = "left"
    winner = left_driver

print(f"The winner is {side} with total time: {winner:.1f}")
