"""
class unreliablecar inherits from car:
    description: car that might not drive depending on reliability.

    function __init__(name, fuel, reliability):
        call car's __init__ with name and fuel
        set reliability attribute (0-100)

    function drive(distance):
        generate random chance between 0 and 100
        if chance < reliability:
            return parent's drive(distance)
        else:
            return 0 (did not drive)
"""
import random
from car import Car

class UnreliableCar(Car):
    """A Car that may not always drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize with name, fuel, and reliability (0-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability; return actual distance driven."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0