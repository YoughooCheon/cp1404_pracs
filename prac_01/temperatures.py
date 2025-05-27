"""
cp1404/cp5632 - practical
temperature conversion program

display menu
get choice
convert choice to uppercase

while choice is not "Q"
    if choice is "C"
        get celsius
        calculate fahrenheit = celsius * 9.0 / 5 + 32
        display fahrenheit
    else if choice is "F"
        get fahrenheit
        calculate celsius = 5 / 9 * (fahrenheit - 32)
        display celsius
    else
        display "invalid option"
    display menu
    get choice
    convert choice to uppercase

display "thank you"
"""

menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(menu)
    choice = input(">>> ").upper()

print("Thank you.")
