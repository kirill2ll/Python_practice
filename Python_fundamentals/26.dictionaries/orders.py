# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product.


prices = {}
quantities = {}

while True:
    current_input = input().split()
    if current_input[0] == "buy":
        break

    product = current_input[0]
    price = float(current_input[1])
    quantity = int(current_input[2])

    if product not in quantities.keys():
        quantities[product] = 0
        prices[product] = 0

    quantities[product] += quantity
    prices[product] = price

for product_name, quantity in quantities.items():
    total_price = quantities[product_name] * prices[product_name]
    print(f"{product_name} -> {total_price:.2f}")

