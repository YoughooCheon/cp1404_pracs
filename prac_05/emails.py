"""
CP1404/CP5632 Practical
Emails and Names Dictionary

function main:
    create empty dictionary email_to_name
    set running to True

    while running:
        prompt user to enter email
        remove leading/trailing spaces from email

        if email is blank:
            set running to False
        else:
            call extract_name function with email to get name

            prompt user: "Is your name [name]? (Y/n)"
            convert response to lowercase and remove spaces

            if response is 'n':
                prompt user to enter their correct name

            store email and name in email_to_name dictionary

    print "Stored emails and names:"
    for each email, name in email_to_name:
        print "name (email)"

function extract_name(email):
    split email at '@' and get the part before '@' (local part)
    split local part at '.' to get list of name parts
    capitalize each name part
    join the capitalized parts with spaces
    return the resulting string as the name

start program by calling main
"""
def main():
    """Main function to collect emails and names and store them in a dictionary."""
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation == 'n':
            name = input("Name: ").strip()

        email_to_name[email] = name

    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract a properly capitalized name from an email address."""
    local_part = email.split('@')[0]
    parts = local_part.split('.')
    name_parts = [part.capitalize() for part in parts]
    return " ".join(name_parts)

if __name__ == "__main__":
    main()