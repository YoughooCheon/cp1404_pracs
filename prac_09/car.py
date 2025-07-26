"""

"""
class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialize with name and fuel, and set odometer to 0."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string showing name, fuel, and odometer."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a certain distance or until fuel runs out; update odometer and fuel."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
