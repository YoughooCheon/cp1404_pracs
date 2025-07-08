"""
import programminglanguage from programming_language

function main()
  create python as ProgrammingLanguage("Python", "Dynamic", true, 1991)
  create ruby as ProgrammingLanguage("Ruby", "Dynamic", true, 1995)
  create visual_basic as ProgrammingLanguage("Visual Basic", "Static", false, 1991)

  print python

  create list languages containing python, ruby, visual_basic

  print "The dynamically typed languages are:"
  for each language in languages
    if language.is_dynamic() is true
      print language.name

if this script is the main program being run
  main()
"""

from programming_language import ProgrammingLanguage

def main():
    """Create and display programming languages and show dynamically typed ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
