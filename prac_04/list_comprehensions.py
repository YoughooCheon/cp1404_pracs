"""
CP1404/CP5632 Practical
List comprehensions

set names list
set full_names list

define list first_initials as first letter of each name in names
print first_initials

define list full_initials as first letters of first and last name in full_names
print full_initials

define list a_names as names starting with 'A' from names
print a_names

print names sorted and joined by space

define list lowercase_full_names as each full_name in lowercase
print lowercase_full_names

set almost_numbers list

define list numbers as integers converted from almost_numbers
print numbers

define list greater_than_nine as numbers greater than 9
print greater_than_nine

define string last_names as last names from full_names longer than 11 characters joined by ', '
print last_names
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension that creates a new list containing the first letter of each name
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension that creates a list containing the initials
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# List comprehension to select only the names that start with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# Creating a single string from the sorted names
print(" ".join(sorted(names)))

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# List comprehension to create a list of integers from the above list of strings
numbers = [int(num) for num in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers that are greater than 9
greater_than_nine = [num for num in numbers if num > 9]
print(greater_than_nine)

# List comprehension to create a string of the last names for those full names longer than 11 characters
last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(last_names)
