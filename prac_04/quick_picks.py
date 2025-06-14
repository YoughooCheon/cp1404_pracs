"""
CP1404/CP5632 Practical
Quick picks

constants
    numbers_per_pick = 6
    min_number = 1
    max_number = 45

function generate_quick_pick
    pick = empty list
    while length of pick < numbers_per_pick
        num = random integer between min_number and max_number
        if num not in pick
            add num to pick
    sort pick in ascending order
    return pick
end function

function main
    prompt "How many quick picks? "
    try
        count = read integer input
    catch error
        print "please enter a valid number."
        exit function

    for i from 1 to count
        pick = generate_quick_pick()
        print pick numbers with two spaces aligned
end function

main
"""

import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    """Return a sorted list of unique random numbers."""
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in pick:
            pick.append(num)
    pick.sort()
    return pick

def main():
    """Ask user for number of picks and print them."""
    try:
        count = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for _ in range(count):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

main()