# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(num):
    for i in range(1, num):
        num *= i

    return num

num1 = int(input())
num2 = int(input())

num1_fac = factorial(num1)
num2_fac = factorial(num2)

print(f"{num1_fac/num2_fac:.2f}")