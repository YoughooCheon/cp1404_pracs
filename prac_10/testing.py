"""
function repeat_string takes a string and a number
    return the string repeated with spaces in between

function is_long_word takes a word and an optional length (default is 5)
    return true if the length of the word is greater than or equal to the given length

function format_phrase takes a phrase
    remove leading and trailing spaces and capitalize the first letter
    if the phrase does not end with a period
        add a period to the end
    return the formatted phrase

function run_tests
    check if repeating "hi" two times gives "hi hi"
    create a car object with default fuel
    check if its fuel is 0
    check if its odometer is 0
    create another car object with fuel set to 50
    check if its fuel is 50

run the run_tests function
run the doctest module to test functions using embedded test cases
"""
import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_phrase(phrase):
    """
    Format a phrase as a sentence.

    >>> format_phrase("hello")
    'Hello.'
    >>> format_phrase("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase("already formatted.")
    'Already formatted.'
    """
    phrase = phrase.strip().capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase

def run_tests():
    assert repeat_string("hi", 2) == "hi hi"
    car = Car()
    assert car.fuel == 0
    assert car._odometer == 0
    car2 = Car(fuel=50)
    assert car2.fuel == 50

run_tests()
doctest.testmod()
