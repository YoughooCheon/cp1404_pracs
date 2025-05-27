"""
CP1404/CP5632 - Practical
menus conversion program

get name

display menu
get choice

while choice != "Q"
    if choice == "H"
        display "Hello" + name
    else if choice == "G"
        display "Goodbye" + name
    else
        display "Invalid choice"
    display menu
    get choice

display "Finished."
"""
MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")
