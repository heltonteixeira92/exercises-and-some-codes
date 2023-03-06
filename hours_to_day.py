hours = int(input('type hours quantity'))

days = 0

if hours > 24:
    while hours >= 24:
        days += 1
        hours -= 24

print(days)
