"""
function main():
    languages = []
    open file 'languages.csv' for reading as in_file
    read and ignore header line
    for each line in in_file:
        split line by ','
        set reflection to true if third part is 'Yes'
        create language object with name, typing, reflection, and year
        add language to languages list
    close in_file

    for each language in languages:
        print language

main()

function using_csv():
    open file 'languages.csv' for reading as in_file
    read and ignore header line
    create csv reader from in_file
    for each row in reader:
        print row
    close in_file

function using_namedtuple():
    open file 'languages.csv' for reading as in_file
    read header line and split into field names
    print field names
    define namedtuple 'language' with fields: name, typing, reflection, year
    create csv reader from in_file
    for each row in reader:
        create language from row using _make
        print language using repr
    close in_file

function using_csv_namedtuple():
    define namedtuple 'language' with fields: name, typing, reflection, year
    open file 'languages.csv' for reading as in_file
    read and ignore header line
    for each language in map _make over csv reader of in_file:
        print language.name + ' was released in ' + language.year
        print repr(language)
"""
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)

main()

def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()

def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))
