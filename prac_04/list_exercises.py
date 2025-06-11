# list_exercises.py

NUM_FIXED_INPUTS = 5  # Constant declaration

def print_number_stats(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# Part 1: Fixed input of 5 numbers
def part1_fixed_5_numbers():
    numbers = []
    for _ in range(NUM_FIXED_INPUTS):
        num = int(input("Number: "))
        numbers.append(num)
    print_number_stats(numbers)


# Part 2: Username check
def part2_username_check():
    USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your username: ")
    print("Access granted" if username in USERNAMES else "Access denied")


# Part 3: Input numbers until negative number entered
def part3_indefinite_numbers():
    numbers = []
    count = 1
    while True:
        num = int(input(f"Number {count}: "))
        if num < 0:
            break
        numbers.append(num)
        count += 1

    if numbers:
        print_number_stats(numbers)
    else:
        print("No positive numbers were entered.")


# Part 4: Print repeated strings
def part4_repeated_strings():
    strings = []
    while True:
        s = input("Enter a string (blank to finish): ")
        if s == "":
            break
        strings.append(s)

    repeated = set()
    seen = set()
    for s in strings:
        if s in seen:
            repeated.add(s)
        else:
            seen.add(s)

    if repeated:
        print("Strings repeated: " + ", ".join(repeated))
    else:
        print("No repeated strings entered")


# Part 5: Memberwise addition of two lists
def add_memberwise(list1, list2):
    length = max(len(list1), len(list2))
    return [(list1[i] if i < len(list1) else 0) + (list2[i] if i < len(list2) else 0) for i in range(length)]


# Main function
def main():
    print("== Part 1: Fixed 5 numbers ==")
    part1_fixed_5_numbers()

    print("\n== Part 2: Username check ==")
    part2_username_check()

    print("\n== Part 3: Indefinite numbers until negative ==")
    part3_indefinite_numbers()

    print("\n== Part 4: Repeated strings ==")
    part4_repeated_strings()

    print("\n== Part 5: Memberwise addition example ==")
    print(add_memberwise([1, 2, 3], [4, 5, 6]))
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))

# Directly call main()
main()
