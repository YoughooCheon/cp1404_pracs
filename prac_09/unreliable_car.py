import random
from car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar with name, fuel, and reliability (0-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car if a random number < reliability. Return distance driven (may be 0)."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
