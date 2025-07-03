"""
Estimate time: 15 minutes
Start time: 2025-07-03 14:00

This module defines the ProgrammingLanguage class, which stores basic information
about a programming language including its typing discipline, whether it supports
reflection, and the year it first appeared.

Actual time: 12 minutes
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
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
