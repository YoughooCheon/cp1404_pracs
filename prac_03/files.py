"""
CP1404/CP5632 - Practical
Files handling exercises: practice reading and writing files using various methods.

print ("Enter your name: ")
name = user input

open file "name.txt" for writing
write name to file
close file

open file "name.txt" for reading
name_from_file = read whole file, then remove whitespace
close file

print("Hi ", name_from_file, "!")

open file "numbers.txt" for reading
first_number = read first line as integer
second_number = read second line as integer
close file

print(first_number + second_number)

total = 0
open file "numbers.txt" for reading
for each line in file
    total = total + integer value of line (remove whitespace)
close file

print(total)
"""

name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    print(first_number + second_number)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)
