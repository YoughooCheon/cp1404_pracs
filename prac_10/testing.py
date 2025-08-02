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
