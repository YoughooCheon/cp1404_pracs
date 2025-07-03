"""
class car

  function __init__(name="", fuel=0)
    set name
    set fuel
    set odometer to 0

  function add_fuel(amount)
    add amount to fuel

  function drive(distance)
    if distance > fuel
      set distance to fuel
      set fuel to 0
    else
      subtract distance from fuel
    add distance to odometer
    return distance

  function __str__()
    return "name, fuel=fuel, odometer=odometer"
"""
class Car:

    def __init__(self, name="", fuel=0):
        """Initialize a Car instance with a name and optional fuel."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add a specified amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance or until fuel runs out."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
