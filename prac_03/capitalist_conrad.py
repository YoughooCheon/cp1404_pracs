"""
CP1404/CP5632 - Practical
Stock price simulator with daily volatile changes.
Outputs day count and price, writes output to file.

max_increase = 0.175
max_decrease = 0.05
min_price = 1.0
max_price = 100.0
initial_price = 10.0
filename = "capitalist_conrad_output.txt"

price = initial_price
day_count = 0

open filename for writing as out_file

print "Starting price: $" + format price to 2 decimals to out_file
print "Starting price: $" + format price to 2 decimals

while price >= min_price and price <= max_price
    day_count = day_count + 1
    if random integer between 1 and 2 equals 1 then
        price_change = random float between 0 and max_increase
    else
        price_change = random float between -max_decrease and 0

    price = price * (1 + price_change)

    output_line = "On day " + day_count + " price is: $" + format price to 2 decimals
    print output_line to out_file
    print output_line

close out_file
"""

import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = 'capitalist_conrad_output.txt'

price = INITIAL_PRICE
day_count = 0

out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:.2f}", file=out_file)
print(f"Starting price: ${price:.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    day_count += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    output_line = f"On day {day_count} price is: ${price:.2f}"
    print(output_line, file=out_file)
    print(output_line)

out_file.close()
