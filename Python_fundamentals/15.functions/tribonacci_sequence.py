# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1.
# You will receive a positive integer number as input.

def tribonacci(number_times):
    num1 = 1
    num2 = 0
    num3 = 0
    for i in range(1, number_times + 1):
        num4 = num1 + num2 + num3
        print(num4, end=" ")

        num1 = num2
        num2 = num3
        num3 = num4


number = int(input())
tribonacci(number)
