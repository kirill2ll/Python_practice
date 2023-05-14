number_of_lines = int(input())

even_numbers = set()
odd_numbers = set()

name_to_sum = [sum([ord(ch) for ch in input()]) / (line + 1) for line in range(number_of_lines)]

{even_numbers.add(int(num)) if int(num) % 2 == 0 else odd_numbers.add(int(num)) for num in name_to_sum}

if sum(even_numbers) == sum(odd_numbers):
    print(", ".join([str(num) for num in even_numbers.union(odd_numbers)]))
elif sum(odd_numbers) > sum(even_numbers):
    print(", ".join([str(num) for num in odd_numbers.difference(even_numbers)]))
else:
    print(", ".join([str(num) for num in odd_numbers.symmetric_difference(even_numbers)]))

# chr(97) - a (asci table 97 = a)
# ord('a') - 97 (obratnij variant chrf

