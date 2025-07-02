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
