#the solution is not over, because of unclear requirements

num_str = input()
num2_str = input()
num1 = int(num_str)
num2 = int(num2_str)
for num in range(num1, num2):
    for i in (str(num)):
        if int(i) == 0:
            break
        elif int(i) % 2 == 0:
            break
    else:
        print(num)

