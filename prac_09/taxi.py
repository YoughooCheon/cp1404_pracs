"""
class car:
    description: simple car with name, fuel, and odometer.

    function __init__(name, fuel):
        set car's name
        set car's fuel amount
        initialize odometer to 0

    function drive(distance):
        if requested distance > fuel:
            limit distance to fuel amount
        subtract distance from fuel
        add distance to odometer
        return distance driven

    function __str__():
        return string showing name, fuel, and odometer

class taxi (inherits from car):
    description: car subclass that tracks fare based on distance driven.

    class variable price_per_km = 1.23

    function __init__(name, fuel):
        call car's __init__ with name and fuel
        initialize current_fare_distance to 0

    function drive(distance):
        distance_driven = call parent's drive(distance)
        add distance_driven to current_fare_distance
        return distance_driven

    function get_fare():
        return current_fare_distance multiplied by price_per_km

    function start_fare():
        reset current_fare_distance to 0

    function __str__():
        return parent's string plus current fare distance and price per km info
"""
class Car:
    """A simple car class with fuel and odometer."""

    def __init__(self, name, fuel):
        """Initialise car with name and fuel."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        """Drive the car for given distance or until fuel runs out."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """Return car details as string."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

class Taxi(Car):
    """Car subclass that tracks fare cost based on distance."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise taxi with name and fuel."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive taxi and update current fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def get_fare(self):
        """Calculate current fare based on distance driven."""
        return self.current_fare_distance * self.price_per_km

    def start_fare(self):
        """Reset fare distance to zero for new trip."""
        self.current_fare_distance = 0

    def __str__(self):
        """Return taxi details including current fare info."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"
