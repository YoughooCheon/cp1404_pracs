"""
class musician:
    description: represents a musician with a name and a collection of instruments.

    function __init__(name):
        set musician's name
        initialize instruments as empty list

    function __str__():
        return string showing musician's name and instruments list

    function __repr__():
        return string representation of musician's instance variables

    function add(instrument):
        add the instrument to the musician's instruments list

    function play():
        if instruments list is empty:
            return message that musician needs an instrument
        else:
            return string stating musician is playing the first instrument in the list

main block:
    import Guitar class

    create musician instance
    check musician's name is empty string
    check musician's instruments list is empty

    set musician's name
    add two Guitar instances to musician's instruments list
    print musician's info
    print musician playing their instrument
"""
class Musician:
    """Musician class"""

    def __init__(self, name=""):
        """Construct a Musician with a name and empty instrument collection."""
        self.name = name
        self.instruments = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({self.instruments})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, instrument):
        """Add an instrument to musician's collection."""
        self.instruments.append(instrument)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.instruments:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.instruments[0]}"

if __name__ == '__main__':
    from guitar import Guitar

    musician = Musician()
    assert musician.name == ""
    assert musician.instruments == []

    musician.name = "Lincoln Brewster"
    musician.instruments.append(Guitar("Fender Lincoln Brewster Stratocaster", 2020, 3419.0))
    musician.instruments.append(Guitar("Ernie Ball Music Man Silhouette Special", 1993, 2499.0))
    print(musician)
    print(musician.play())