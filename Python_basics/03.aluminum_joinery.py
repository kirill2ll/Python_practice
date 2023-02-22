joinery_number = int(input())
joinery_type = input()
delivery_type = input()

output = None
price = 0

if joinery_type == "90X130":
    price = 110 * joinery_number
    if 60 > joinery_number > 30:
        price *= 0.95
    elif joinery_number > 60:
        price *= 0.92
elif joinery_type == "100X150":
    price = 140 * joinery_number

    if 80 > joinery_number > 40:
        price *= 0.94
    elif joinery_number > 80:
        price *= 0.90
elif joinery_type == "130X180":
    price = 190 * joinery_number

    if 50 > joinery_number > 20:
        price *= 0.93
    elif joinery_number > 50:
        price *= 0.88
elif joinery_type == "200X300":
    price = 250 * joinery_number

    if 50 > joinery_number > 25:
        price *= 0.91
    elif joinery_number > 50:
        price *= 0.86

if delivery_type == "With delivery":
    price += 60

if joinery_number > 99:
    price *= 0.96

if joinery_number < 10:
    output = "Invalid order"
else:
    output = f"{price:.2f} BGN"

print(output)

