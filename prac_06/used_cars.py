"""
import car from car.py

function main()
  create car object limo with name "limo" and fuel 100
  add 20 fuel to limo
  print limo's fuel
  drive limo 115 km and store distance driven
  print distance driven
  print limo

if this file is the main program
  main()
"""

from car import Car

def main():
    """Run the used car simulation with simple steps."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km.")
    print(limo)

if __name__ == "__main__":
    main()
