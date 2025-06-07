"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started

min_length = 2
max_length = 6
is_special_character_required = false
special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

function main()
    display "please enter a valid password"
    display "your password must be between", min_length, "and", max_length, "characters, and contain:"
    display "    1 or more uppercase characters"
    display "    1 or more lowercase characters"
    display "    1 or more numbers"
    if is_special_character_required is true then
        display "    and 1 or more special characters: ", special_characters

    password = get user input

    while not is_valid_password(password)
        display "invalid password!"
        password = get user input

    display "your", length of password, "-character password is valid:", password

function is_valid_password(password)
    if length of password < min_length or length of password > max_length then
        return false

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for each character in password
        if character is lowercase then
            number_of_lower = number_of_lower + 1
        else if character is uppercase then
            number_of_upper = number_of_upper + 1
        else if character is digit then
            number_of_digit = number_of_digit + 1
        else if character is in special_characters then
            number_of_special = number_of_special + 1

    if number_of_lower = 0 or number_of_upper = 0 or number_of_digit = 0 then
        return false

    if is_special_character_required is true and number_of_special = 0 then
        return false

    return true

main
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Check minimum counts for lowercase, uppercase, digit
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # If special character required, check count
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    return True

main()
