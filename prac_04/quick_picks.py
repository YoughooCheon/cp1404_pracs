import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
ERROR_MSG_INVALID = "Invalid input. Please enter a valid integer."
ERROR_MSG_NEGATIVE = "Please enter a positive integer."

def generate_quick_pick():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in pick:
            pick.append(num)
    pick.sort()
    return pick

def get_num_picks():
    while True:
        try:
            n = int(input("How many quick picks? "))
            if n <= 0:
                print(ERROR_MSG_NEGATIVE)
            else:
                return n
        except ValueError:
            print(ERROR_MSG_INVALID)

# Program starts here
num_picks = get_num_picks()
for _ in range(num_picks):
    pick = generate_quick_pick()
    print(" ".join(f"{num:2d}" for num in pick))
