"""
cp1404/cp5632 - practical
Shop Calculator conversion program

print "Shop Calculator Program"

get number_of_items

while number_of_items < 0
    print "Invalid number of items!"
    get number_of_items

set total_price to 0

for each item from 1 to number_of_items
    get price_of_item
    total_price = total_price + price_of_item

if total_price > 100 then
    total_price = total_price * 0.9  # 10% discount 적용

print "Total price for", number_of_items, "items is $", total_price formatted to 2 decimals
"""
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # 10% discount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
