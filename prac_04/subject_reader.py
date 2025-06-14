"""
CP1404/CP5632 Practical
Data file -> lists program

function main
    load_data and store result in data
    display_subject_details with data

function load_data
    define empty list data_list
    open file FILENAME for reading as input_file
    for each line in input_file
        remove newline characters from line
        split line by comma into parts
        convert parts[2] (student count) to integer
        append parts to data_list
    close file
    return data_list

function display_subject_details(data)
    for each subject, lecturer, student_count in data
        print "{subject} is taught by {lecturer} and has {student_count} students"

main
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data_list.append(parts)
    return data_list

def display_subject_details(data):
    """Display subject details in the required format."""
    for subject, lecturer, student_count in data:
        print(f"{subject} is taught by {lecturer} and has {student_count} students")

main()
