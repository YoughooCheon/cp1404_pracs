"""
class ProgrammingLanguage

function create_programming_language(name, typing, reflection, year):
    language = {
        "name": name,
        "typing": typing,
        "reflection": reflection,
        "year": year
    }
    return language

function get_language_string(language):
    return language["name"] + ", " + language["typing"] + " typing, reflection=" + str(language["reflection"]) + ", first appeared in " + str(language["year"])

function is_dynamic(language):
    return language["typing"] == "dynamic"

function run_tests():
    ruby = create_programming_language("ruby", "dynamic", true, 1995)
    python = create_programming_language("python", "dynamic", true, 1991)
    visual_basic = create_programming_language("visual basic", "static", false, 1991)

    languages = [ruby, python, visual_basic]

    print get_language_string(python)

    print "the dynamically typed languages are:"

    for each language in languages:
        if is_dynamic(language):
            print language["name"]

function main():
    run_tests()

main()
"""
class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()
