"""

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
