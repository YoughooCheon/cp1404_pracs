"""
class ProgrammingLanguage:
    function __init__(name, typing, reflection, pointer_arithmetic):
        set self.name = name
        set self.typing = typing
        set self.reflection = reflection
        set self.pointer_arithmetic = pointer_arithmetic

    function __repr__():
        return string formatted as:
            "{name}, {typing} Typing, Reflection={reflection}, Pointer Arithmetic={pointer_arithmetic}"

    function is_dynamic():
        return True if self.typing.lower() == "dynamic", else False

function run_tests():
    create ruby as ProgrammingLanguage("Ruby", "Dynamic", True, False)
    create python as ProgrammingLanguage("Python", "Dynamic", True, False)
    create visual_basic as ProgrammingLanguage("Visual Basic", "Static", False, False)
    create c_lang as ProgrammingLanguage("C", "Static", False, True)

    languages = list of [ruby, python, visual_basic, c_lang]

    print python  # calls python.__repr__()

    print "The dynamically typed languages are:"

    for each language in languages:
        if language.is_dynamic():
            print language.name

function main():
    run_tests()

main()
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, False)
    c_lang = ProgrammingLanguage("C", "Static", False, True)

    languages = [ruby, python, visual_basic, c_lang]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()