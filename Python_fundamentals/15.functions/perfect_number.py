# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# "We have a perfect number!" - if the number is perfect.
# "It's not so perfect." - if the number is NOT perfect.


def is_perfect_number(num):
    sum = 0
    for i in range(1, int(num/2) + 1):  #int(num/2) + 1 is used for optimization
        if num % i == 0:
            sum += i

    if sum == num:
        return True
    else:
        return False


number = int(input())

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


