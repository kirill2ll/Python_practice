# Social Distribution
# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".


#functions
def numbers_are_wealth(numbers, min_wealth):
    are_wealth = True

    for num in numbers:
        if num < min_wealth:
            are_wealth = False
            break

    return are_wealth


def redistribute_wealth(numbers, min_wealth):
    max_num = max(numbers)
    min_num = min(numbers)
    difference_min_and_wealth = min_wealth - min_num

    #adding wealth to the min number
    for i in range(len(numbers)):
        if numbers[i] == min_num:
            numbers[i] += difference_min_and_wealth
            break

    #removing difference from the max number
    for i in range(len(numbers)):
        if numbers[i] == max_num:
            numbers[i] -= difference_min_and_wealth
            break

    return numbers



#input
numbers = list(map(int, input().split(", ")))
min_wealth = int(input())


#main logic
if sum(numbers)/len(numbers) < min_wealth:
    print("No equal distribution possible")
else:
    while numbers_are_wealth(numbers, min_wealth) != True:
        numbers= redistribute_wealth(numbers, min_wealth)
    else:
        print(numbers)

