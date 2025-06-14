"""
CP1404/CP5632 Practical
List warmup

define a list called numbers with the values [3, 1, 4, 1, 5, 9, 2]

write comments predicting the results of these expressions:
    numbers[0]
    numbers[-1]
    numbers[3]
    numbers[:-1]
    numbers[3:4]
    5 in numbers
    7 in numbers
    "3" in numbers
    numbers + [6, 5, 3]

change the first element of numbers to "ten"
change the last element of numbers to 1

print all elements of numbers except the first two
print whether 9 is an element in numbers
print the final state of numbers (optional)
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted results (before running the code)
# numbers[0]       → 3
# numbers[-1]      → 2
# numbers[3]       → 1
# numbers[:-1]     → [3, 1, 4, 1, 5, 9]
# numbers[3:4]     → [1]
# 5 in numbers     → True
# 7 in numbers     → False
# "3" in numbers   → False
# numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element to "ten" (string, not number)
numbers[0] = "ten"

# Change the last element to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)

# (Optional) Print final list to confirm changes
print(numbers)