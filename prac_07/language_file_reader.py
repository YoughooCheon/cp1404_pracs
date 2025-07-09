"""
import csv module
import namedtuple from collections module
import ProgrammingLanguage class from programming_language module

function main():
    create empty list languages
    open 'languages.csv' for reading as in_file
    read and ignore header line

    for each line in in_file:
        split line by ','
        set reflection to True if third part equals 'Yes', otherwise False
        set pointer_arithmetic to True if fourth part equals 'Yes', otherwise False
        create language object with name, typing, reflection, pointer_arithmetic
        add language object to languages list

    close in_file

    for each language in languages:
        print language

function using_csv():
    open 'languages.csv' for reading as in_file
    read and ignore header line
    create csv reader from in_file

    for each row in reader:
        print row

    close in_file

function using_namedtuple():
    open 'languages.csv' for reading as in_file
    read header line and split by ',' into field names
    print field names
    define namedtuple Language with these field names
    create csv reader from in_file

    for each row in reader:
        create language namedtuple by calling _make with row
        print language using repr

    close in_file

function using_csv_namedtuple():
    open 'languages.csv' for reading as in_file
    read and ignore header line
    define namedtuple Language with fields matching header line

    for each language in map Language._make over csv reader of in_file:
        print language.name + ' was released in ' + language.year
        print repr(language)

    close in_file

main()
"""
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r') as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "True"
            pointer_arithmetic = parts[3] == "True"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)

def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        next(in_file)  # skip header
        reader = csv.reader(in_file)
        for row in reader:
            print(row)

def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        headers = in_file.readline().strip().split(',')
        print(headers)
        Language = namedtuple('Language', [h.strip() for h in headers])
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    with open('languages.csv', 'r') as in_file:
        headers = in_file.readline().strip().split(',')
        Language = namedtuple('Language', [h.strip() for h in headers])
        for language in map(Language._make, csv.reader(in_file)):
            print(language.name, 'has pointer arithmetic:', language.pointer_arithmetic)
            print(repr(language))

if __name__ == '__main__':
    main()
