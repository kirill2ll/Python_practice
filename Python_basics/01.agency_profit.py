company_name = input()
number_adult_tickets = int(input())
number_kids_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

kid_ticket_price = adult_ticket_price * 0.3
full_adult_price = adult_ticket_price + service_fee
full_kid_price = kid_ticket_price + service_fee

all_ticket_price = full_kid_price * number_kids_tickets + full_adult_price * number_adult_tickets

agency_profit = all_ticket_price * 0.2

output = f"The profit of your agency from {company_name} tickets is {agency_profit:.2f} lv."

print(output)
