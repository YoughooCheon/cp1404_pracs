"""
class guitar:
    description: stores details of a guitar including name, year, and cost.

    function __init__(name, year, cost):
        set guitar's name
        set guitar's year of manufacture
        set guitar's cost

    function __str__():
        return a formatted string with name, year, and cost

    function __repr__():
        return string representation (same as __str__)

    function get_age():
        calculate and return guitar's age using current year constant

    function is_vintage():
        return true if guitar's age is greater than or equal to vintage age constant

    function __lt__(other):
        return true if this guitar's year is less than the other guitar's year (for sorting)
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a string representation of a Guitar."""
        return str(self)

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
