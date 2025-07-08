"""

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
