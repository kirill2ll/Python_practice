# Write a program that calculates the total cost of bought furniture. You will be given information about each purchase on separate lines until you receive the command "Purchase". Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
import re

#pattern = r">>([A-Za-z0-9]+)<<([\.\d+]+)!(\d+)"
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
items = []
total_price = 0
while True:

    line = input()

    if line =="Purchase":
        break

    results = re.search(pattern, line)


    if results:
        furniture, price, quantity = results.groups()
        items.append(furniture)
        total_price += float(price) * int(quantity)


print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total_price:.2f}")