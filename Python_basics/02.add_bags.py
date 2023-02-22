baggage_price_over20 = float(input())
baggage_kg = float(input())
days_before_trip = int(input())
baggage_number = int(input())

baggage_fee = 0
if baggage_kg < 10:
    baggage_fee = baggage_price_over20 * 0.2
elif baggage_kg <= 20:
    baggage_fee = baggage_price_over20 * 0.5
else:
    baggage_fee = baggage_price_over20

if days_before_trip < 7:
    baggage_fee *= 1.4
elif days_before_trip <= 30:
    baggage_fee *= 1.15
else:
    baggage_fee *= 1.1

total_baggage_fee = baggage_fee * baggage_number
output = f"The total price of bags is: {total_baggage_fee:.2f} lv."
print(output)
