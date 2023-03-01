# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.


items = input().split("|")
budget = float(input())
bought_items = []
total_spend = 0

for item in items:
    item_list = item.split("->")
    type = item_list[0]
    price = float(item_list[1])
    if budget >= price:
        ok_to_buy = (
            (type == "Clothes" and 0 < price <= 50.00) or
            (type == "Shoes" and 0 < price <= 35.00) or
            (type == "Accessories" and 0 < price <= 20.50)
        )
        if ok_to_buy:
            budget -= price
            bought_items.append(price * 1.4)
            total_spend += price

sum_of_items = sum(bought_items)
profit = sum_of_items - total_spend

#output
for price in bought_items:
    print(f"{price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
if sum_of_items + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


