"""
class silverservicetaxi (inherits from taxi):
    description: specialised taxi with fanciness factor and fixed flagfall charge.

    class variable flagfall = 4.50

    function __init__(name, fuel, fanciness):
        call parent taxi __init__ with name and fuel
        set fanciness level
        set price_per_km by scaling parent's price_per_km by fanciness

    function get_fare():
        return parent's fare calculation plus flagfall charge

    function __str__():
        return parent's string representation plus formatted flagfall info
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale the price per km based on fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare for the current trip including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi, with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"