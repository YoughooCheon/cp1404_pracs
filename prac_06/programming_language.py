"""
class programminglanguage

  function __init__(name, typing, reflection, year)
    set self.name to name
    set self.typing to typing
    set self.reflection to reflection
    set self.year to year

  function is_dynamic()
    if lowercase(self.typing) == "dynamic"
      return true
    else
      return false

  function __str__()
    return string:
      self.name + ", " + self.typing + " Typing, Reflection=" + self.reflection + ", First appeared in " + self.year

"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialize the ProgrammingLanguage object with given parameters."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")
