"""
CP1404/CP5632 Practical
List exercises

define constant num_fixed_inputs = 5

function get_valid_int(prompt)
    loop forever
        prompt user with prompt
        if input is integer then
            return integer
        else
            print "invalid input! please enter a number."
        end if
    end loop
end function

function print_number_stats(numbers)
    print first number in numbers
    print last number in numbers
    print smallest number in numbers
    print largest number in numbers
    print average of numbers
end function

function part1_fixed_5_numbers()
    create empty list numbers
    for i from 1 to num_fixed_inputs
        number = get_valid_int("number " + i + ": ")
        add number to numbers
    end for
    print_number_stats(numbers)
end function

function part2_username_check()
    define set usernames with authorized usernames
    prompt user for username
    if username in usernames then
        print "access granted"
    else
        print "access denied"
    end if
end function

function part3_indefinite_numbers()
    create empty list numbers
    count = 1
    loop forever
        number = get_valid_int("number " + count + ": ")
        if number < 0 then
            break loop
        end if
        add number to numbers
        count = count + 1
    end loop

    if numbers is not empty then
        print_number_stats(numbers)
    else
        print "no positive numbers were entered."
    end if
end function

function part4_repeated_strings()
    create empty dictionary seen
    loop forever
        prompt user for string (blank to finish)
        if string is empty then
            break loop
        end if
        increase count of string in seen
    end loop

    create list repeated of strings with count > 1 in seen
    if repeated is not empty then
        print "strings repeated: " + repeated joined by comma
    else
        print "no repeated strings entered."
    end if
end function

function add_memberwise(list1, list2)
    length = max length of list1 and list2
    create empty list result
    for i from 0 to length - 1
        value1 = element i of list1 if exists else 0
        value2 = element i of list2 if exists else 0
        add (value1 + value2) to result
    end for
    return result
end function

function main()
    loop forever
        print menu options
        prompt user for choice
        if choice is "1" then
            call part1_fixed_5_numbers()
        else if choice is "2" then
            call part2_username_check()
        else if choice is "3" then
            call part3_indefinite_numbers()
        else if choice is "4" then
            call part4_repeated_strings()
        else if choice is "5" then
            print add_memberwise([1, 2, 3], [4, 5, 6])
        else if choice is "q" then
            print "exiting the program."
            break loop
        else
            print "invalid option!"
        end if
    end loop
end function

main()
"""

NUM_FIXED_INPUTS = 5  # Constant declaration

def get_valid_int(prompt):
    """Gets a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def print_number_stats(numbers):
    """Prints basic statistics of a list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

def part1_fixed_5_numbers():
    """Collects and analyzes five user-inputted numbers."""
    numbers = [get_valid_int(f"Number {i+1}: ") for i in range(NUM_FIXED_INPUTS)]
    print_number_stats(numbers)

def part2_username_check():
    """Checks if a username is authorized."""
    USERNAMES = {'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'}
    username = input("Enter your username: ")
    print("Access granted" if username in USERNAMES else "Access denied")

def part3_indefinite_numbers():
    """Collects numbers until a negative number is entered."""
    numbers = []
    count = 1
    while True:
        num = get_valid_int(f"Number {count}: ")
        if num < 0:
            break
        numbers.append(num)
        count += 1

    print_number_stats(numbers) if numbers else print("No positive numbers were entered.")

def part4_repeated_strings():
    """Finds and prints repeated strings from user input."""
    seen = {}
    while True:
        s = input("Enter a string (blank to finish): ")
        if s == "":
            break
        seen[s] = seen.get(s, 0) + 1

    repeated = [s for s, count in seen.items() if count > 1]
    print(f"Strings repeated: {', '.join(repeated)}" if repeated else "No repeated strings entered.")

def add_memberwise(list1, list2):
    """Adds elements of two lists index-wise."""
    length = max(len(list1), len(list2))
    return [(list1[i] if i < len(list1) else 0) + (list2[i] if i < len(list2) else 0) for i in range(length)]

def main():
    """Displays a menu and executes selected functions."""
    options = {
        "1": part1_fixed_5_numbers,
        "2": part2_username_check,
        "3": part3_indefinite_numbers,
        "4": part4_repeated_strings,
        "5": lambda: print(add_memberwise([1, 2, 3], [4, 5, 6])),
        "q": lambda: print("Exiting the program.")
    }

    while True:
        print("\n== Available Functions ==")
        print("1 - Enter 5 numbers and display statistics")
        print("2 - Username validation")
        print("3 - Enter numbers until a negative is given")
        print("4 - Identify repeated strings")
        print("5 - Perform element-wise addition on two lists")
        print("q - Quit")

        choice = input("Select an option: ")
        if choice in options:
            options[choice]()
            if choice == "q":
                break
        else:
            print("Invalid option! Please select a valid number.")

main()

