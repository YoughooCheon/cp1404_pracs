"""
define main
    set password to result of get_password function
    run print_asterisks function with password as argument
end main

define get_password
    prompt user to enter a password
    while password length is less than min_length
        display error message
        prompt user to re-enter password
    return password
end get_password

define print_asterisks(password)
    display asterisks equal to the length of password
end print_asterisks

run main
"""
MIN_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
