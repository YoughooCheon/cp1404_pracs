"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.

guitar_name ← "gibson l-5 ces"
guitar_year ← 1922
guitar_cost ← 16035.9

display "my guitar: " + guitar_name + ", first made in " + guitar_year as string

display formatted string using .format() with values in order
display formatted string using .format() with positional indexes
display formatted string using .format() with repeated index

display same sentence using f-string formatting with variables

format guitar_cost to include comma and 2 decimal places
display formatted cost using f-string

numbers ← [1, 19, 123, 456, -25]
for i from 1 to length of numbers
    number ← numbers[i - 1]
    display "number i is number", with number right-aligned in 5-character space using f-string

format guitar_cost to include comma and no decimal places
display guitar_year, guitar_name, and formatted guitar_cost using f-string

for i from 0 to 10
    power ← 2 ^ i
    display "2 ^ i is power", with i right-aligned in 2 spaces and power right-aligned in 4 spaces using f-string
"""

GUITAR_NAME = "Gibson L-5 CES"
GUITAR_YEAR = 1922
GUITAR_COST = 16035.9

print("My guitar: " + GUITAR_NAME + ", first made in " + str(GUITAR_YEAR))

print("My guitar: {}, first made in {}".format(GUITAR_NAME, GUITAR_YEAR))
print("My guitar: {0}, first made in {1}".format(GUITAR_NAME, GUITAR_YEAR))
print("My {0} was first made in {1} (that's right, {1}!)".format(GUITAR_NAME, GUITAR_YEAR))

# And with f-string formatting
print(f"My {GUITAR_NAME} was first made in {GUITAR_YEAR} (that's right, {GUITAR_YEAR}!)")

formatted_cost = f"${GUITAR_COST:,.2f}"
print(f"My {GUITAR_NAME} would cost {formatted_cost}")

numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

print(f"{GUITAR_YEAR} {GUITAR_NAME} for about ${GUITAR_COST:,.0f}!")

for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
