# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. Use filter().


def find_even(numbers):
    result = list(filter(lambda x: int(x) % 2 == 0, numbers))
    return result
numbers = list(map(int, input().split(" ")))
print(find_even(numbers))