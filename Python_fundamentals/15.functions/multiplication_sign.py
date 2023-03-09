# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

def count_minuses(numbers):
    minus_count = 0
    zero = False
    for num in numbers:
        if num < 0:
            minus_count += 1
        elif num == 0:
            zero = True
            break

    if zero:
        return "zero"
    if minus_count % 2 == 0:
        return "positive"
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(count_minuses([num1, num2, num3]))