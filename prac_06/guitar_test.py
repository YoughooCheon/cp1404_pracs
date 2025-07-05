"""
import Guitar class from guitar module

function main()
  create gibson as Guitar("Gibson L-5 CES", 1922, 16035.40)
  create another as Guitar("Another Guitar", 2013, 500)

  print "Gibson L-5 CES get_age() - Expected 102. Got actual age from get_age()"
  print "Another Guitar get_age() - Expected 11. Got actual age from get_age()"

  print "Gibson L-5 CES is_vintage() - Expected True. Got actual result from is_vintage()"
  print "Another Guitar is_vintage() - Expected False. Got actual result from is_vintage()"

if this script is the main program being run
  main()
"""

from guitar import Guitar

def main():
    """Test Guitar class methods: get_age() and is_vintage()."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 11. Got {another.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

if __name__ == "__main__":
    main()