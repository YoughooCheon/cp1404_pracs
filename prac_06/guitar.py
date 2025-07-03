"""
Estimate time: 15 minutes
Start time: 2025-07-03 15:00

This module defines the Guitar class for storing and working with guitar data.

Actual time: 13 minutes
"""

from datetime import datetime

CURRENT_YEAR = datetime.now().year

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if guitar is 50 years or older."""
        return self.get_age() >= 50
