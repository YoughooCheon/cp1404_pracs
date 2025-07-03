"""
Estimate time: 20 minutes
Start time: 2025-07-03 15:18

Allows user to input guitars, store them, and display with formatting.

Actual time: 16 minutes
"""

from guitar import Guitar

print("My guitars!")
guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.\n")
    name = input("Name: ")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
