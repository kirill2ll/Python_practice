days = int(input())
hours = int(input())
total_sum = 0

for day in range(1, days+1):
    sum_to_pay_today = 0

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
               sum_to_pay_today += 2.5

        elif day % 2 != 0 and hour % 2 == 0:
                sum_to_pay_today += 1.25

        else:
            sum_to_pay_today += 1

    total_sum += sum_to_pay_today
    print(f"Day: {day} - {sum_to_pay_today:.2f} leva")

print(f"Total: {total_sum:.2f} leva")
