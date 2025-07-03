"""
Estimate time: 10 minutes
Start time: 2025-07-03 14:12

This script uses the ProgrammingLanguage class to create instances of several
languages and prints details about them, especially those that use dynamic typing.

Actual time: 8 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

languages = [python, ruby, visual_basic]

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
