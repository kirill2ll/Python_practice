import sys


def find_min(numbers):
    min = sys.maxsize
    for num in numbers:
        if num != 0 and num < min:
            min = num

    return min

cables = list(map(int, input().split(" ")))

total_trims = 0

while cables.count(0) != len(cables):
    min_num = find_min(cables)

    for i in range(len(cables)):
        if cables[i] != 0:
            cables[i] -= min_num
            total_trims += 1




print(total_trims)