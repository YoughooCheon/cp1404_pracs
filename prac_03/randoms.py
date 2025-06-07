"""
randoms.py
Practice using the random module.

low_int = 5
high_int = 20
start_odd = 3
stop_odd = 10
step = 2
low_float = 2.5
high_float = 5.5

random_integer = random integer between low_int and high_int inclusive
display random_integer

random_odd = random number from range starting at start_odd, stopping before stop_odd, stepping by step
display random_odd

random_float = random float between low_float and high_float inclusive
display random_float

random_1_to_100 = random integer between 1 and 100 inclusive
display random_1_to_100
"""

import random

# Constants for random ranges
LOW_INT = 5
HIGH_INT = 20
START_ODD = 3
STOP_ODD = 10
STEP = 2
LOW_FLOAT = 2.5
HIGH_FLOAT = 5.5

# Line 1: random integer between 5 and 20 (inclusive)
print(random.randint(LOW_INT, HIGH_INT))
# Possible smallest number: 5
# Possible largest number: 20

# Line 2: random odd number from range(3, 10) with step of 2 → possible values: 3, 5, 7, 9
print(random.randrange(START_ODD, STOP_ODD, STEP))
# Possible smallest number: 3
# Possible largest number: 9
# Could this line produce a 4? No, because step=2 and starting from 3 → it skips even numbers.

# Line 3: random float between 2.5 and 5.5 (inclusive of both ends)
print(random.uniform(LOW_FLOAT, HIGH_FLOAT))
# Possible smallest number: 2.5
# Possible largest number: 5.5
# The result is a float and can include many values between those limits.

# Code to produce a random integer between 1 and 100 (inclusive)
print(random.randint(1, 100))
