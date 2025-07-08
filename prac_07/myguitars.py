"""
import module csv
import guitar class from guitar

function main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print "these are my guitars:"
    display_guitars(guitars)

    sort guitars by year (using guitar_less_than)
    print "\nguitars sorted by year:"
    display_guitars(guitars)

    print "\nadd a new guitar:"
    new_guitar = add_guitar()
    append new_guitar to guitars

    save_guitars(filename, guitars)
    print "\nupdated guitar list saved to file."

function load_guitars(filename):
    guitars = []
    open file filename for reading as file
    create csv reader from file
    for each row in reader:
        name, year, cost = unpack row
        create guitar object with name, int(year), float(cost)
        append guitar to guitars
    close file
    return guitars

function display_guitars(guitars):
    for each guitar in guitars:
        print guitar_to_string(guitar)

function add_guitar():
    name = input "name: "
    year = int(input "year: ")
    cost = float(input "cost: ")
    return create_guitar(name, year, cost)

function save_guitars(filename, guitars):
    open file filename for writing as file
    create csv writer from file
    for each guitar in guitars:
        write row [guitar.name, guitar.year, guitar.cost]
    close file

if program is main:
    main()
"""
import csv
from guitar import Guitar

def main():
    """Main entry point of the program, controls overall flow."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    print("\nAdd a new guitar:")
    new_guitar = add_guitar()
    guitars.append(new_guitar)

    save_guitars(filename, guitars)
    print("\nUpdated guitar list saved to file.")

def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)

def add_guitar():
    """Prompt user for guitar details and return a Guitar object."""
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    return Guitar(name, year, cost)

def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == '__main__':
    main()
