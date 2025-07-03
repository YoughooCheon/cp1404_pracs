"""
Estimate time: 5 minutes
Start time: 2025-07-03 15:13

Tests the Guitar class's get_age() and is_vintage() methods.

Actual time: 4 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2025

guitar1 = Guitar("Gibson L-5 CES", 1925, 16035.40)
guitar2 = Guitar("Another Guitar", 2016, 500.00)

print(f"{guitar1.name} get_age() - Expected {CURRENT_YEAR - 1925}. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected {CURRENT_YEAR - 2016}. Got {guitar2.get_age()}")

print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
