"""
import Guitar class from guitar module

function main()
  print "My guitars!"
  create empty list called guitars

  prompt user for name
  while name is not empty
    prompt user for year (as integer)
    prompt user for cost (as float)
    create guitar using name, year, cost
    add guitar to guitars list
    print "guitar added"
    prompt user for next name

  print "These are my guitars:"
  for each guitar in guitars with index starting from 1
    if guitar is vintage
      set vintage_label to " (vintage)"
    else
      set vintage_label to empty string
    print "Guitar i: guitar name, year, cost formatted with vintage label"

if this script is the main program being run
  main()
"""
from guitar import Guitar

def main():
    """Collect guitars from user and display them."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_label = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_label}")

if __name__ == "__main__":
    main()