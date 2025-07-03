"""
class Guitar

  function __init__(name="", year=0, cost=0)
    set name
    set year
    set cost

  function get_age()
    get current year from system date
    return current year - year

  function is_vintage()
    if get_age() >= 50
      return True
    else
      return False

  function __str__()
    return "name (year) : $cost" formatted with 2 decimal places and commas
"""
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return age of the guitar based on the current year."""
        from datetime import date
        return date.today().year - self.year

    def is_vintage(self):
        """Return True if guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __str__(self):
        """Return string representation like: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"