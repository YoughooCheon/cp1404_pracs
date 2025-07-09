"""
function Guitar

function create_guitar(name, year, cost):
    guitar = {
        "name": name,
        "year": year,
        "cost": cost
    }
    return guitar

function guitar_to_string(guitar):
    return guitar["name"] + " (" + str(guitar["year"]) + ") : $" + format(guitar["cost"], ".2f")

function guitar_less_than(guitar1, guitar2):
    return guitar1["year"] < guitar2["year"]
"""
class Guitar:
    """Represent a Guitar with name, year, and cost."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Compare Guitars by year for sorting (oldest to newest)."""
        return self.year < other.year
